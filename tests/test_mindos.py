import importlib.util,io,json,unittest,zipfile,hashlib
from pathlib import Path
s=importlib.util.spec_from_file_location('mindos',Path(__file__).resolve().parents[1]/'scripts/mindos.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class PackageTests(unittest.TestCase):
 def fixture(self):return {p.name:p.read_bytes() for p in (Path(__file__).resolve().parents[1]/'examples/mindos').iterdir()}
 def archive(self,files):
  b=io.BytesIO()
  with zipfile.ZipFile(b,'w') as z:
   for n,v in files.items():z.writestr(n,v)
  return b.getvalue()
 def test_valid(self):self.assertEqual(m.validate(self.archive(self.fixture()))['format'],'mindos')
 def test_tamper(self):
  f=self.fixture();f['README.md']+=b'changed'
  with self.assertRaises(ValueError):m.validate(self.archive(f))
 def test_path(self):
  f=self.fixture();f['../escape']=b'x'
  with self.assertRaises(ValueError):m.validate(self.archive(f))
 def test_duplicate(self):
  b=io.BytesIO(self.archive(self.fixture()))
  with zipfile.ZipFile(b,'a') as z:z.writestr('manifest.json','{}')
  with self.assertRaises(ValueError):m.validate(b.getvalue())
 def test_oversized(self):
  f=self.fixture();f['README.md']=b'a'*(1024*1024+1)
  with self.assertRaises(ValueError):m.validate(self.archive(f))

 def test_agents_format(self):
  f={p.name:p.read_bytes() for p in (Path(__file__).resolve().parents[1]/'examples/mindos-agents').iterdir()}
  self.assertEqual(m.validate(self.archive(f))['formatVersion'],'0.2')
  platform=json.loads(f['platforms.json']);platform['agents']['operations']=['records.delete'];f['platforms.json']=json.dumps(platform).encode()
  manifest=json.loads(f['manifest.json']);manifest['files']['platforms.json']=hashlib.sha256(f['platforms.json']).hexdigest();f['manifest.json']=json.dumps(manifest).encode()
  with self.assertRaises(ValueError):m.validate(self.archive(f))
