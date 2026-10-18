#!/usr/bin/env python3
"""Local mindOS package validator/packer. Standard library, no network."""
import argparse, hashlib, io, json, re, stat, struct, uuid, zipfile
from pathlib import Path
FILES={'manifest.json','MINDPRINT.md','tokens.json','app.json','data.json','backend.json','platforms.json','README.md'}
MAX_ARCHIVE=2*1024*1024
MAX_EXPANDED=4*1024*1024
SLUG=re.compile(r'[a-z][a-z0-9-]{0,39}')
def require(ok,message):
    if not ok: raise ValueError(message)
def obj(value,keys):
    require(isinstance(value,dict) and set(value)==set(keys),'Unexpected object fields')
def text(v,maximum=200):
    require(isinstance(v,str) and 0<len(v)<=maximum,'Invalid text')
def slug(v):
    require(isinstance(v,str) and SLUG.fullmatch(v),'Invalid identifier')
def unique(items):
    require(len(items)==len(set(items)),'Duplicate identifiers')
def validate_files(files):
    require(set(files)==FILES,'Package must contain exactly the eight required files')
    require(sum(map(len,files.values()))<=MAX_EXPANDED,'Expanded package too large')
    for v in files.values():
        require(len(v)<=1024*1024,'Entry too large');v.decode('utf-8',errors='strict')
    m=json.loads(files['manifest.json']);obj(m,['format','formatVersion','id','version','name','reviewStatus','files'])
    require(m['format']=='mindos' and m['formatVersion'] in ['0.1','0.2'],'Unsupported format')
    require(str(uuid.UUID(m['id']))==m['id'],'Invalid UUID');require(re.fullmatch(r'\d+\.\d+\.\d+',m['version']),'Invalid version');text(m['name'],80)
    require(m['reviewStatus'] in ['draft','reviewed','synthetic'],'Invalid review status')
    require(set(m['files'])==FILES-{'manifest.json'},'Invalid digest list')
    for n in m['files']: require(hashlib.sha256(files[n]).hexdigest()==m['files'][n],'Digest mismatch')
    require(files['README.md'].decode().strip(),'Missing README')
    require(files['MINDPRINT.md'].decode().startswith('<!-- mindprint-spec: 0.1 -->'),'Unsupported MINDPRINT')
    text(files['README.md'].decode(),1024*1024)
    t=json.loads(files['tokens.json']);obj(t,['colors','typography','spacing','radius']);obj(t['colors'],['background','foreground','accent','surface'])
    for c in t['colors'].values():require(isinstance(c,str) and re.fullmatch(r'#[a-fA-F0-9]{6}',c),'Invalid color')
    obj(t['typography'],['family','bodySize']);require(t['typography']['family']=='system','Unsupported font')
    for v,lo,hi in [(t['typography']['bodySize'],14,24),(t['spacing'],4,32),(t['radius'],0,32)]:require(type(v)==int and lo<=v<=hi,'Invalid token')
    d=json.loads(files['data.json']);obj(d,['schemaVersion','collections']);require(type(d['schemaVersion'])==int and d['schemaVersion']==1,'Unsupported data schema');require(isinstance(d['collections'],list) and 1<=len(d['collections'])<=12,'Invalid collections')
    for c in d['collections']:
        obj(c,['id','title','fields']);slug(c['id']);text(c['title'],80);require(isinstance(c['fields'],list) and 1<=len(c['fields'])<=12,'Invalid fields')
        for f in c['fields']:
            obj(f,['id','label','type','required']);slug(f['id']);text(f['label'],80);require(f['type']=='text' and type(f['required'])==bool,'Invalid field type')
        unique([f['id'] for f in c['fields']])
    ids=[c['id'] for c in d['collections']];unique(ids)
    a=json.loads(files['app.json']);obj(a,['screens']);require(isinstance(a['screens'],list) and 1<=len(a['screens'])<=12,'Invalid screens')
    for s in a['screens']:
        obj(s,['id','title','collection','kind']);slug(s['id']);text(s['title'],80);require(s['collection'] in ids and s['kind']=='collection','Invalid screen collection')
    unique([s['id'] for s in a['screens']])
    require(json.loads(files['backend.json'])=={'contract':'mindos-records-v1','auth':'owner-scoped','sync':'append-only'},'Unsupported backend')
    p=json.loads(files['platforms.json']);obj(p,['web','ios','macos','agents'] if m['formatVersion']=='0.2' else ['web','ios','macos'])
    for v in [p[k] for k in ['web','ios','macos']]:
        obj(v,['navigation','typography','components'])
        for x in v.values():text(x,2000)
    if m['formatVersion']=='0.2':
        a=p['agents'];obj(a,['protocol','operations','instructions'])
        require(a['protocol']=='mcp','Unsupported agent protocol');text(a['instructions'],2000)
        ops=a['operations'];require(isinstance(ops,list) and 1<=len(ops)<=2 and all(x in ['records.read','records.append'] for x in ops),'Invalid agent operations');unique(ops);require('records.read' in ops,'Agent read capability required')
    return m

def validate(blob):
    require(len(blob)<=MAX_ARCHIVE,'Archive too large')
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        infos=z.infolist();require(len(infos)==8 and {i.filename for i in infos}==FILES,'Invalid entries')
        require(sum(i.file_size for i in infos)<=MAX_EXPANDED,'Expanded package too large')
        for i in infos:
            require(i.file_size<=1024*1024 and not (i.flag_bits & ~2048) and i.compress_type in (0,8),'Unsafe entry')
            require(not stat.S_ISLNK(i.external_attr>>16),'Symlink forbidden')
            require(i.header_offset+30<=len(blob),'Missing local header')
            header=struct.unpack_from('<IHHHHHIIIHH',blob,i.header_offset)
            require(header[0]==0x04034b50 and header[2]==i.flag_bits and header[3]==i.compress_type and header[6]==i.CRC and header[7]==i.compress_size and header[8]==i.file_size,'ZIP headers disagree')
        return validate_files({i.filename:z.read(i) for i in infos})

def pack(folder,output):
    paths=list(folder.iterdir());require({p.name for p in paths}==FILES,'Unexpected folder entries')
    require(all(p.is_file() and not p.is_symlink() and p.stat().st_size<=1024*1024 for p in paths),'Unsafe source files')
    files={p.name:p.read_bytes() for p in paths};m=json.loads(files['manifest.json']);m['files']={n:hashlib.sha256(v).hexdigest() for n,v in files.items() if n!='manifest.json'};files['manifest.json']=(json.dumps(m,indent=2)+'\n').encode();validate_files(files)
    out=io.BytesIO()
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for n,v in sorted(files.items()):z.writestr(n,v)
    validate(out.getvalue())
    with output.open('xb') as f:f.write(out.getvalue())

if __name__=='__main__':
    p=argparse.ArgumentParser();s=p.add_subparsers(dest='command',required=True);v=s.add_parser('validate');v.add_argument('file',type=Path);v=s.add_parser('pack');v.add_argument('folder',type=Path);v.add_argument('--output',required=True,type=Path);args=p.parse_args()
    try:
        if args.command=='validate':require(args.file.stat().st_size<=MAX_ARCHIVE,'Archive too large');validate(args.file.read_bytes());print('Structure and digests valid; review privacy and fidelity separately.')
        else:pack(args.folder,args.output);print('Package created. Review before sharing.')
    except (ValueError,OSError,KeyError,TypeError,zipfile.BadZipFile,UnicodeError,struct.error) as e:raise SystemExit('Invalid package or source: '+type(e).__name__)
