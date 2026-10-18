import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("mindprint", ROOT / "scripts/mindprint.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.profile = self.root / "sample-mind"
        self.profile.mkdir()
        for name in m.FILES:
            (self.profile / name).write_text((ROOT / "examples/sample-mind" / name).read_text())

    def test_clean_bundle_is_allowlisted_and_portable(self):
        output = self.root / "bundle.zip"
        m.pack(self.profile, output, True, [])
        with zipfile.ZipFile(output) as z:
            self.assertEqual(set(z.namelist()), {f"sample-mind/{n}" for n in (*m.FILES, "MIND.md")})
            plain = z.read("sample-mind/MIND.md").decode()
            self.assertIn("# A fictional creative collaborator", plain)
            self.assertNotIn("name: sample-mind", plain)

    def test_requires_review_assertion(self):
        with self.assertRaises(ValueError):
            m.pack(self.profile, self.root / "bundle.zip", False, [])

    def test_private_extra_file_blocks_pack(self):
        (self.profile / "raw-chat.txt").write_text("private inputs")
        with self.assertRaises(ValueError):
            m.pack(self.profile, self.root / "bundle.zip", True, [])

    def test_hidden_input_blocks_pack(self):
        (self.profile / ".private").mkdir()
        self.assertTrue(m.inspect_profile(self.profile, [])[1])

    def test_symlink_blocks_pack(self):
        p = self.profile / "ABOUT.md"
        p.unlink()
        outside = self.root / "source.txt"
        outside.write_text("sensitive")
        p.symlink_to(outside)
        self.assertTrue(m.inspect_profile(self.profile, [])[1])

    def test_sensitive_patterns_report_no_matched_values(self):
        private = "private.person@example.test"
        (self.profile / "ABOUT.md").write_text(private)
        _, issues = m.inspect_profile(self.profile, [])
        self.assertTrue(issues)
        self.assertNotIn(private, " ".join(issues))

    def test_custom_terms_remain_private(self):
        private = "Unpublished Project Alias"
        (self.profile / "ABOUT.md").write_text(private)
        _, issues = m.inspect_profile(self.profile, [private])
        self.assertTrue(issues)
        self.assertNotIn(private, " ".join(issues))

    def test_never_overwrites(self):
        output = self.root / "bundle.zip"
        output.write_bytes(b"existing")
        with self.assertRaises(FileExistsError):
            m.pack(self.profile, output, True, [])
        self.assertEqual(output.read_bytes(), b"existing")

    def test_output_inside_source_rejected(self):
        with self.assertRaises(ValueError):
            m.pack(self.profile, self.profile / "bundle.zip", True, [])

    def test_bad_name_rejected(self):
        p = self.profile / "SKILL.md"
        p.write_text(p.read_text().replace('name: "sample-mind"', 'name: "Sample--Mind"'))
        self.assertTrue(m.inspect_profile(self.profile, [])[1])

    def test_unquoted_or_invalid_yaml_values_rejected(self):
        for value in ("Use this: when deciding", "'unterminated", "null", "123"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                m.split_skill('---\nname: "sample-mind"\ndescription: ' + value + '\n---\n# Rules\nFollow the task.')

    def test_quoted_colon_and_hyphens_are_valid(self):
        meta, body = m.split_skill('---\nname: "sample-mind"\ndescription: "Use this: compare --- alternatives"\n---\n# Rules')
        self.assertEqual(meta["description"], "Use this: compare --- alternatives")
        self.assertEqual(body, "# Rules")

    def test_large_file_rejected(self):
        (self.profile / "ABOUT.md").write_bytes(b"x" * (m.MAX_FILE_BYTES + 1))
        self.assertTrue(m.inspect_profile(self.profile, [])[1])

    def test_standalone_starter_includes_all_guidance(self):
        prompt = m.starter_prompt()
        for name in m.REFERENCES:
            self.assertIn((ROOT / "references" / name).read_text().strip(), prompt)
        self.assertIn("If you cannot access my history, interview me", prompt)


if __name__ == "__main__":
    unittest.main()
