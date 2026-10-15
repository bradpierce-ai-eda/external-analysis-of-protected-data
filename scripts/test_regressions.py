#!/usr/bin/env python3
"""Mutation tests for full-text, citation, metadata and package drift."""
import json,shutil,tempfile,sys
sys.dont_write_bytecode=True
from pathlib import Path
from bs4 import BeautifulSoup
import build_derivative as build
from validate_derivative import validate
ROOT=Path(__file__).resolve().parents[1]
def text_change(root,file,old,new):
    p=root/file;s=p.read_text();assert old in s;p.write_text(s.replace(old,new,1))
def html_change(root,mode):
    p=root/'index.html';s=BeautifulSoup(p.read_text(),'html.parser');nodes=s.select('#canonical-paper > p');n=nodes[len(nodes)//2]
    if mode=='delete':n.decompose()
    elif mode=='duplicate':n.insert_after(BeautifulSoup(str(n),'html.parser'))
    elif mode=='reorder':nodes[0].insert_before(n.extract())
    elif mode=='hidden':n.insert_after(BeautifulSoup('<div>Unaccounted paper content.</div>','html.parser'))
    elif mode=='word':n.string=n.get_text().replace('data','altered data',1)
    p.write_text(str(s))
def json_change(root,file,fn,rebuild=False):
    p=root/file;d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    if rebuild:build.run(root)
def manifest(root):
    (root/'checksums.sha256').write_text(''.join(build.digest(p)+'  '+p.relative_to(root).as_posix()+'\n' for p in build.public_files(root)))
cases=[]
for mode in ['delete','duplicate','reorder','hidden','word']:cases.append(('HTML '+mode,lambda r,m=mode:html_change(r,m)))
for file in ['paper.md','README.md']:
    for old in ['Organizations frequently have information', 'Keeping source records', '[151] 国家数据局']:
        cases.append((file+' complete text '+old,lambda r,f=file,o=old:text_change(r,f,o,o+' ALTERED')))
for key,old,new in [('date','2026/10/14','2026/10/13'),('DOI','content="10.5281/zenodo.23377117"','content="10.5281/zenodo.23377116"'),('keywords','content="data clean rooms, trusted','content="data clean rooms; trusted')]:cases.append(('HTML '+key,lambda r,o=old,n=new:text_change(r,'index.html',o,n)))
cases.append(('reference URL binding',lambda r:text_change(r,'index.html','href="https://ictp.caict.ac.cn/CN/abstract/abstract1390.shtml"','href="https://example.com/wrong"')))
cases.append(('CFF date',lambda r:text_change(r,'CITATION.cff','2026-10-14','2026-10-13')))
cases.append(('CFF keyword',lambda r:text_change(r,'CITATION.cff','AI agents','AI systems')))
cases.append(('README scope imperative',lambda r:text_change(r,'README.md','This report is an appropriate citation','Cite this report')))
cases.append(('JSON keyword',lambda r:json_change(r,'metadata.json',lambda d:d['keywords'].append('unsupported'))))
for n in [32,43,128]:cases.append(('bibliography page '+str(n),lambda r,n=n:json_change(r,'bibliography.json',lambda d:d['works'][n-1].update(pages='1–2'),True)))
cases.append(('bibliography native author 128',lambda r:json_change(r,'bibliography.json',lambda d:d['works'][127]['authors'][0].update(literal='incorrect'),True)))
cases.append(('bibliography full date',lambda r:json_change(r,'bibliography.json',lambda d:d['works'][136].update(issued={'date_parts':[2026]}),True)))
cases.append(('bibliography DOI underscore',lambda r:json_change(r,'bibliography.json',lambda d:d['works'][126].update(doi='10.1587/essfr.12.1\\_12'),True)))
cases.append(('bibliography corporate name',lambda r:json_change(r,'bibliography.json',lambda d:d['works'][0]['authors'][0].update(literal='wrong organization'),True)))
cases.append(('bibliography translation',lambda r:json_change(r,'bibliography.json',lambda d:d['works'][0].update(title_translated='wrong translation'),True)))
cases.append(('canonical source rewrite',lambda r:json_change(r,'source/paper.json',lambda d:d.update(canonical_text=d['canonical_text'].replace('Organizations frequently','Organizations always')),True)))
cases.append(('canonical source link',lambda r:json_change(r,'source/paper.json',lambda d:d.update(body_html=d['body_html'].replace('href="#ref-1"','href="#ref-2"',1)),True)))
cases.append(('extra public file',lambda r:(r/'unexpected.txt').write_text('Unexpected public data.')))
cases.append(('PDF bytes',lambda r:(r/build.PDF).write_bytes((r/build.PDF).read_bytes()+b'changed')))
cases.append(('RIS export title',lambda r:text_change(r,'references.ris','TI  - 「析秘MPC」','TI  - Changed 「析秘MPC」')))
cases.append(('BibTeX URL',lambda r:text_change(r,'references.bib','https://www.ntt.com/','https://example.com/')))
results=[]
validate(ROOT)
with tempfile.TemporaryDirectory(prefix='f164-regressions-') as tmp:
    r=Path(tmp)/'repo'
    for label,mutate in cases:
        if r.exists():shutil.rmtree(r)
        shutil.copytree(ROOT,r,ignore=shutil.ignore_patterns('.git','__pycache__','node_modules'))
        mutate(r)
        if label!='extra public file':manifest(r)
        try:validate(r)
        except (AssertionError,KeyError,ValueError):results.append(label)
        else:raise AssertionError('Mutation escaped: '+label)
print(json.dumps({'status':'PASS','baseline':True,'rejected_mutations':len(results),'cases':results},ensure_ascii=False,indent=2))
