const fs=require('fs'),path=require('path'),assert=require('assert');
const {Cite}=require('@citation-js/core');require('@citation-js/plugin-bibtex');require('@citation-js/plugin-csl');require('@citation-js/plugin-ris');
const root=path.resolve(process.argv[2]||path.join(__dirname,'..'));
const data=JSON.parse(fs.readFileSync(path.join(root,'bibliography.json'),'utf8'));
const name=a=>a.literal||[a.given,a['non-dropping-particle'],a.family].filter(Boolean).join(' ');
const norm=s=>(s||'').normalize('NFC');
let checks=0;
for(const file of ['references.bib','references.csl.json','references.ris']){
  const parsed=new Cite(fs.readFileSync(path.join(root,file),'utf8')).data;
  assert.equal(parsed.length,data.works.length,file+' count');
  assert.deepEqual(parsed.map(r=>r.id),data.works.map(w=>w.citekey),file+' ordered IDs');
  for(let i=0;i<parsed.length;i++){
    const r=parsed[i],w=data.works[i],label=file+' '+w.id;
    assert.equal(norm(r.title),norm(w.title),label+' native title');
    assert.equal(r.URL,w.url,label+' opaque URL');
    assert.equal(r.DOI||null,w.doi||null,label+' opaque DOI');
    assert.deepEqual(r.author.map(name).map(norm),w.authors.map(name).map(norm),label+' authors');
    assert.deepEqual(r.issued?.['date-parts']?.[0]||null,w.issued?.date_parts||null,label+' full date precision');
    if(w.container_title)assert.equal(norm(r['container-title']),norm(w.container_title),label+' container');
    if(w.pages)assert.equal(r.page.replace(/–/g,'-'),w.pages.replace(/–/g,'-'),label+' pages');
    if(w.title_translated)assert((r.note||'').includes(w.title_translated),label+' separate English translation');
    if(w.editors){
      if(file==='references.ris')for(const a of w.editors)assert((r.note||'').includes(name(a)),label+' editors in parsed RIS note');
      else assert.deepEqual(r.editor.map(name),w.editors.map(name),label+' editors');
    }
    checks+=9;
  }
}
const paper=JSON.parse(fs.readFileSync(path.join(root,'metadata.json'),'utf8'));
const own=new Cite(fs.readFileSync(path.join(root,'citation.bib'),'utf8')).data;
assert.equal(own.length,1);assert.equal(own[0].title,paper.title);assert.equal(own[0].DOI,paper.doi);assert.deepEqual(own[0].issued['date-parts'][0],[2026,10,14]);assert.equal(own[0].URL,'https://doi.org/'+paper.doi);
console.log(JSON.stringify({status:'PASS',processor:'Citation.js',formats:3,works:data.works.length,checks,paper_citation:'PASS'}));
