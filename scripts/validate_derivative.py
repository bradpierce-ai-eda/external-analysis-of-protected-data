#!/usr/bin/env python3
"""Full publication, metadata, bibliography and public-tree validation."""
import argparse,hashlib,json,re,unicodedata,sys
sys.dont_write_bytecode=True
from pathlib import Path
from bs4 import BeautifulSoup,Comment
from pypdf import PdfReader
import yaml
import build_derivative as build
PDF_HASH='6d6ecdf9d44e18f296844af01b0dd55facbc8a3f09c358638f0c4cf7b1f97892'
TEXT_HASH='ec37769439ce0264e0d64e370a9dd80269c48a06fbe51c5f328ffe4099924e5f'
MD_HASH='b82918e4458dd803b4dd45039eb46dfc63696c8b559a4f8f9c7c8a829ffa0dfb'
def norm(s):return ' '.join(unicodedata.normalize('NFC',s).replace('\u2060','').split())
def lines(s):return [norm(v) for v in s.splitlines() if v.strip()]
def require(ok,msg):
    if not ok:raise AssertionError(msg)
def hashtext(s):return hashlib.sha256(s.encode()).hexdigest()
def html_blocks(soup):
    result=[];nodes=soup.select('h1,h2,h3,h4,h5,h6,p,li');selected={id(n) for n in nodes}
    for n in nodes:
        require(not any(id(p) in selected for p in n.parents),'Nested canonical text block')
        text=n.get_text()
        if n.name=='li':
            m=re.fullmatch(r'ref-(\d+)',n.get('id',''));require(m,'Unexpected canonical list item');text='['+m[1]+'] '+text
        result.append(norm(text))
    for s in soup.find_all(string=True):
        if isinstance(s,Comment) or not norm(str(s)):continue
        require(any(id(p) in selected for p in s.parents),'Unaccounted canonical text')
    return result
def validate(root):
    p=json.loads((root/'source/paper.json').read_text());inv=json.loads((root/'source/invariants.json').read_text());meta=json.loads((root/'metadata.json').read_text());data=json.loads((root/'bibliography.json').read_text())
    require(build.digest(root/'bibliography.json')=='e35154e87f9a5f10dc7f05ea80b4fb9195bbe1b9e71999a3bf43d805e5855316','Frozen adjudicated bibliography changed')
    require(hashtext(p['canonical_text'])==TEXT_HASH,'Canonical source text changed')
    require(hashtext(p['canonical_markdown'])==MD_HASH,'Canonical source Markdown changed')
    require(hashtext(p['front_html'])=='f6f33a6658ebc219381de5f519b901e1ee0d602b6cefff4927b347206187e608','Frozen front HTML changed')
    require(hashtext(p['body_html'])=='f22632fb06dc263e1152b639d5ee5eeca0cf062173f6f620c59bb6362bdfccc4','Frozen body HTML changed')
    expected=lines(p['canonical_text']);require(len(expected)==313,'Canonical block count')
    require(lines((root/'paper.md').read_text())==expected,'Complete Markdown text mismatch')
    readme=(root/'README.md').read_text();marker='## Canonical paper text\n\n';require(readme.count(marker)==1,'README canonical delimiter')
    require(lines(readme.split(marker)[1])==expected,'Complete README text mismatch')
    soup=BeautifulSoup((root/'index.html').read_text(),'html.parser');front=soup.select('#scholarly-front-matter');main=soup.select('#canonical-paper');scope=soup.select('#relevance-and-citation-scope')
    require(len(front)==len(main)==len(scope)==1,'Unique page partitions')
    combined=BeautifulSoup(str(front[0])+str(main[0]),'html.parser')
    require(html_blocks(combined)==expected,'Complete HTML text mismatch')
    require([n.get_text() for n in scope[0].select('p')]==p['relevance_and_citation_scope'],'HTML scope text drift')
    require('## Relevance and citation scope\n\n'+'\n\n'.join(p['relevance_and_citation_scope']) in readme,'README scope drift')
    bodyhtml=str(soup.body);require(bodyhtml.index('id="scholarly-front-matter"')<bodyhtml.index('id="relevance-and-citation-scope"')<bodyhtml.index('id="canonical-paper"'),'Front matter order')
    require(front[0].select_one('h1').get_text()==p['title'],'Title first')
    require(front[0].select_one('.author').get_text()=='Brad Pierce','Visible human author')
    require(norm(front[0].select_one('.abstract p').get_text())==norm(p['abstract']),'Full visible abstract')
    require(front[0].select_one('.keywords').get_text().removeprefix('Keywords: ')==', '.join(p['keywords']),'Visible keyword commas/order')
    require(str(front[0]).index('class="abstract"')<str(front[0]).index('class="keywords"'),'Keywords after abstract')
    tags={'citation_title':p['title'],'citation_author':'Brad Pierce','citation_publication_date':'2026/10/14','citation_doi':p['doi'],'citation_pdf_url':build.URL+build.PDF,'citation_fulltext_html_url':build.URL,'keywords':', '.join(p['keywords'])}
    for key,value in tags.items():require([n['content'] for n in soup.select('meta[name="'+key+'"]')]==[value],'Metadata '+key)
    require([n['href'] for n in soup.select('link[rel="canonical"]')]==[build.URL],'Self-canonical URL')
    schema=json.loads(soup.select_one('script[type="application/ld+json"]').string)
    require(schema['headline']==p['title'] and schema['alternativeHeadline']==p['subtitle'],'Structured titles')
    require(schema['datePublished']==p['date']=='2026-10-14' and schema['identifier']=='https://doi.org/'+p['doi'],'Structured date/DOI')
    require(schema['keywords']==meta['keywords']==p['keywords'],'Structured keyword consistency')
    z=json.loads((root/'source/zenodo-record.json').read_text());zm=z['metadata']
    require(z['is_published'] and z['id']=='23377117','Published Zenodo record identity')
    require(zm['publication_date']==meta['publication_date']==p['date'],'Zenodo date consistency')
    require([s['subject'] for s in zm['subjects'] if not s.get('scheme')]==p['keywords'],'Zenodo keyword consistency')
    cff=yaml.safe_load((root/'CITATION.cff').read_text());require(cff['keywords']==p['keywords'] and cff['doi']==p['doi'] and cff['date-released']==p['date'],'CFF consistency')
    require(cff['preferred-citation']['date-published']==p['date'] and cff['preferred-citation']['doi']==p['doi'],'Preferred CFF citation')
    require(cff['license']==meta['license']==p['license']=='CC-BY-NC-4.0','License consistency')
    refs=soup.select('li[id^="ref-"]');require(len(refs)==151,'Reference count')
    for n,(node,slot) in enumerate(zip(refs,data['reference_slots']),1):
        raw='['+str(n)+'] '+node.get_text();require(raw==slot['raw_reference'],'Exact reference '+str(n))
        require(hashtext(raw)==slot['raw_reference_sha256'],'Reference source hash '+str(n))
        require(node['id']=='ref-'+str(n),'Reference sequence')
        require([a['href'] for a in node.select('a')]==slot['published_urls'],'Reference URL targets '+str(n))
    anchors=soup.select('a.citeref');require(len(anchors)==227,'Citation link count')
    ids=[n.get('id') for n in soup.select('[id]')];require(len(ids)==len(set(ids)),'Duplicate HTML anchors')
    for a in soup.select('a[href]'):
        href=a['href']
        if href.startswith('#'):require(href[1:] in ids,'Broken internal anchor')
        elif not re.match(r'https?://',href):require((root/href).is_file(),'Missing relative resource '+href)
    require(sum(len(n.select('a')) for n in refs)==152,'Reference URL count')
    require(not soup.select('img,table,figure'),'Unexpected visual object')
    require(not re.search(r'\bAccessed\b|\bretrieved on\b',' '.join(n.get_text() for n in refs),re.I),'Reader access date')
    works=data['works'];wids={w['id'] for w in works};sids={s['id'] for s in data['reference_slots']};links=data['reference_work_links']
    require(len(wids)==len(works)==151,'Unique works');require(len({w['citekey'] for w in works})==151,'Unique citekeys')
    require({l['work_id'] for l in links}==wids and {l['reference_slot_id'] for l in links}==sids,'No orphan works/slots')
    dois=[w['doi'].lower() for w in works if w.get('doi')];require(len(dois)==len(set(dois)),'Unique DOIs')
    require(data['reference_slots'][126]['classification']=='alternate-locator' and len(works[126]['alternate_urls'])==1,'Reference 127 mapping')
    require([a['literal'] for a in works[127]['authors']]==['白玉真','贾轩','王思源','袁博'],'Reference 128 names')
    for n,pages in [(32,'97–106'),(43,'301–325'),(128,'34–39')]:require(works[n-1]['pages']==pages,'Verified page range '+str(n))
    require(sum(bool(w['title_translated']) for w in works)==93,'Translation count')
    require(all(w.get('accessed') is None for w in works),'Public retrieval dates absent')
    for w in works:
        require(w['title'] and w['authors'] and w['url'],'Required reusable fields '+w['id'])
        require(all(a.get('literal') or a.get('family') for a in w['authors']),'Author identity '+w['id'])
        require(all(k in w['field_provenance'] for k in ['title','authors','issued','url']),'Field provenance '+w['id'])
        if not w['issued']:require(any(e['kind']=='undated' and e['slot']==int(w['reference_slots'][0][-3:]) for e in data['exceptions']),'Explicit undated exception')
    pdf=root/build.PDF;require(build.digest(pdf)==PDF_HASH and pdf.stat().st_size==692912,'Published PDF byte identity')
    reader=PdfReader(pdf);require(len(reader.pages)==23,'Published PDF pages')
    require(reader.metadata.title==p['title'] and reader.metadata.author=='Brad Pierce','PDF title/author metadata')
    require(reader.metadata.get('/Subject')==p['subtitle'] and reader.metadata.get('/Keywords')==', '.join(p['keywords']),'PDF subtitle/keyword metadata')
    pdftext=' '.join((p.extract_text() or '') for p in reader.pages)
    require(all(s in pdftext for s in [p['title'],'Brad Pierce','October 14, 2026','Keywords:','白玉真']),'Searchable publication identity')
    require(len(pdftext)>60000,'Searchable complete PDF')
    additions=readme.split(marker)[0]+'\n'+scope[0].get_text()+'\n'+soup.select_one('#repository-resources').get_text()+'\n'+json.dumps(meta,ensure_ascii=False)+'\n'+(root/'provenance.json').read_text()+'\n'+(root/'CITATION.cff').read_text()
    additions+='\n'+json.dumps({k:data[k] for k in ['adjudications','exceptions','normalization_policy','pilot','completeness']},ensure_ascii=False)+'\n'+(root/'LICENSE.md').read_text()
    for phrase in ['when to cite this report','cite this report','you should','ignore previous','system prompt','as an ai','instructions for ai']:
        require(phrase not in additions.lower(),'Prompt-like repository framing: '+phrase)
    for f in build.public_files(root):require(not any(x in f.parts for x in ['__pycache__','.git','node_modules']) and f.suffix!='.pyc','Transient public path')
    require(not (root/'CNAME').exists(),'Project CNAME absent')
    build.run(root,check=True)
    return {'status':'PASS','canonical_blocks':313,'full_text_copies':['HTML','Markdown','README'],'pdf_sha256':PDF_HASH,'pdf_pages':23,'references':151,'works':151,'translations':93,'internal_citation_links':227,'keywords':8,'date':'2026-10-14','manifest_files':len(build.public_files(root)),'publication_changed':False}
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]);o=a.parse_args();print(json.dumps(validate(o.repo.resolve()),ensure_ascii=False,indent=2))
