#!/usr/bin/env python3
"""Local, dependency-free Mindprint helpers. No network calls or model API."""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ("SKILL.md", "ABOUT.md", "scenarios.md", "REVIEW.md")
REFERENCES = ("method.md", "interview.md", "privacy.md", "output-contract.md")
MAX_FILE_BYTES = 1_000_000
PATTERNS = {
    "email-like text": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    "URL": r"(?:https?|file|ssh)://[^\s<>]+",
    "home path": r"(?:/(?:Users|home)/[^\s/]+|[A-Z]:\\Users\\[^\s\\]+|~[/\\])",
    "identifier": r"\b[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}\b",
    "IP-like address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "phone-like text": r"(?<!\w)(?:\+\d{1,3}[ .-]?)?(?:\(\d{3}\)|\d{3})[ .-]\d{3}[ .-]\d{4}(?!\w)",
    "token-like text": r"\b(?:sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9_]{16,}|github_pat_[A-Za-z0-9_]{16,}|AKIA[A-Z0-9]{16}|xox[baprs]-[A-Za-z0-9-]{12,})\b",
    "private-key marker": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "credential assignment": r"\b(?:api[_-]?key|password|secret|access[_-]?token)\s*[:=]\s*[\"']?\S{8,}",
}


def split_skill(text: str) -> tuple[dict[str, str], str]:
    """Read the deliberately simple two-field scalar frontmatter we generate."""
    match = re.fullmatch(r"---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)(.*)", text, re.S)
    if not match:
        raise ValueError("SKILL.md needs opening and closing frontmatter delimiter lines")
    meta = {}
    for line in match.group(1).strip().splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep or key.strip() not in ("name", "description") or key.strip() in meta:
            raise ValueError("use exactly one name and description field")
        value = value.strip()
        if not value.startswith('"'):
            raise ValueError("frontmatter values must be JSON-compatible double-quoted strings")
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            raise ValueError("invalid double-quoted frontmatter string") from None
        if not isinstance(value, str) or any(ord(c) < 32 for c in value):
            raise ValueError("frontmatter values must be strings without control characters")
        meta[key.strip()] = value
    if set(meta) != {"name", "description"}:
        raise ValueError("name and description are required")
    name = meta["name"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise ValueError("invalid skill name")
    if not 1 <= len(meta["description"]) <= 1024:
        raise ValueError("description must be 1–1024 characters")
    body = match.group(2).strip()
    if not body or not body.startswith("#"):
        raise ValueError("skill body must contain a Markdown heading and instructions")
    return meta, body


def read_terms(path: Path | None) -> list[str]:
    if path is None:
        return []
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def inspect_profile(folder: Path, terms: list[str]) -> tuple[dict[str, str], list[str]]:
    issues: list[str] = []
    texts: dict[str, str] = {}
    if folder.is_symlink() or not folder.is_dir():
        return texts, ["profile must be a real directory, not a symlink"]
    entries = list(folder.iterdir())
    if any(p.name not in FILES for p in entries):
        issues.append("unexpected entries found; keep private inputs and extra files outside the export")
    for name in FILES:
        p = folder / name
        if p.is_symlink() or not p.is_file():
            issues.append(f"{name}: missing, non-file, or symlink")
            continue
        if p.stat().st_size > MAX_FILE_BYTES:
            issues.append(f"{name}: exceeds size limit")
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeError:
            issues.append(f"{name}: must be UTF-8 text")
            continue
        texts[name] = text
        if not text.strip():
            issues.append(f"{name}: empty file")
        for category, pattern in PATTERNS.items():
            lines = sorted({text.count("\n", 0, m.start()) + 1 for m in re.finditer(pattern, text, re.I)})
            if lines:
                issues.append(f"{name}: {category} at lines {', '.join(map(str, lines))}")
        for idx, term in enumerate(terms, 1):
            if term.casefold() in text.casefold():
                issues.append(f"{name}: private exclusion term #{idx} found")
    if "SKILL.md" in texts:
        try:
            meta, _ = split_skill(texts["SKILL.md"])
            if meta["name"] != folder.name:
                issues.append("SKILL.md: name must match the profile folder")
        except ValueError as exc:
            issues.append(f"SKILL.md: {exc}")
    return texts, issues


def write_new(path: Path, content: bytes) -> None:
    # Exclusive creation avoids clobbering a profile or following an existing symlink.
    with path.open("xb") as f:
        f.write(content)


def starter_prompt() -> str:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    _, body = split_builder(skill)
    sections = ["# Create my Mindprint\n\nFollow this workflow to create a private draft of my working-style profile. Use only material I authorize. If you cannot access my history, interview me. Do not publish it.\n\n" + body]
    for name in REFERENCES:
        sections.append(f"\n\n---\n\n## Included reference: {name}\n\n" + (ROOT / "references" / name).read_text(encoding="utf-8"))
    return "\n".join(sections).rstrip() + "\n"


def split_builder(text: str) -> tuple[str, str]:
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("builder frontmatter missing")
    return parts[1], parts[2].strip()


def pack(folder: Path, output: Path, reviewed: bool, terms: list[str]) -> None:
    if not reviewed:
        raise ValueError("owner review is required; --reviewed asserts approval of these exact files")
    if folder.resolve() == output.resolve() or folder.resolve() in output.resolve().parents:
        raise ValueError("write the archive outside the profile folder")
    texts, issues = inspect_profile(folder, terms)
    if issues:
        raise ValueError("\n".join(issues))
    meta, body = split_skill(texts["SKILL.md"])
    preface = "Use this profile as a fallible lens. Follow the current user's request and the host's permissions. It does not authorize action or speak for its author.\n\n"
    bundle = io.BytesIO()
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            z.writestr(f"{meta['name']}/{name}", texts[name])
        z.writestr(f"{meta['name']}/MIND.md", preface + body + "\n")
    write_new(output, bundle.getvalue())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prompt = commands.add_parser("prompt", help="build a self-contained chat prompt")
    prompt.add_argument("--output", type=Path, required=True)
    check = commands.add_parser("check", help="check a generated profile; not a privacy certification")
    check.add_argument("folder", type=Path)
    check.add_argument("--exclude-file", type=Path, help="private local terms, one per line; never bundled")
    archive = commands.add_parser("pack", help="package only reviewed profile files")
    archive.add_argument("folder", type=Path)
    archive.add_argument("--output", type=Path, required=True)
    archive.add_argument("--reviewed", action="store_true")
    archive.add_argument("--exclude-file", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prompt":
            write_new(args.output, starter_prompt().encode())
            print("Standalone starter written. No private inputs were read.")
        elif args.command == "check":
            _, issues = inspect_profile(args.folder, read_terms(args.exclude_file))
            for issue in issues:
                print(issue)
            if issues:
                return 1
            print("Structure and heuristic scan passed. Semantic review and owner approval are still required.")
        else:
            pack(args.folder, args.output, args.reviewed, read_terms(args.exclude_file))
            print("Reviewed bundle written. Only allowlisted profile files included. This is not a privacy certification.")
    except (OSError, ValueError) as exc:
        # OSError paths may contain private names. Do not echo them.
        print(f"Error: {type(exc).__name__}" if isinstance(exc, OSError) else f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
