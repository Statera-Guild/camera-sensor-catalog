from pathlib import Path
import csv,re
r=Path(__file__).resolve().parent
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
rows=read(r/'validation_framework/integration/master_catalog_0001_0140.csv')
ids=[x['component_id'] for x in rows]
assert ids==[f'CMP-CAM-{i:04d}' for i in range(1,141)]
assert len({(x['manufacturer'].strip().casefold(),x['model'].strip().casefold()) for x in rows})==140
assert len({(x['manufacturer'].strip().casefold(),x['orderable_sku'].strip().casefold()) for x in rows})==140
for x in rows:
 assert (r/'component_cards'/f"{x['component_id']}.md").exists()
 assert x['manufacturer_evidence_url'].startswith('https://')
for a in range(1,136,5):
 b=a+4;d=r/f'validation_framework/wave_a/batch_{a:04d}_{b:04d}'
 for name in ['inventory.csv','source_registry.csv','specification_claims.csv','manufacturer_evidence_claims.csv','algorithm_compatibility.csv']:
  assert (d/name).exists(),str(d/name)
 assert [x['component_id'] for x in read(d/'inventory.csv')]==[f'CMP-CAM-{i:04d}' for i in range(a,b+1)]
readme=(r/'README.md').read_text(encoding='utf-8')
assert readme.count('## Component Index')==1
assert readme.count('<!-- CAMERA_CATALOG_START -->')==1
assert readme.count('<!-- CAMERA_CATALOG_END -->')==1
assert 'PAI-SG-CAMERA-CATALOG:START' not in readme
assert len(re.findall(r'^\| \[CMP-CAM-\d{4}\]',readme,re.M))==140
for cid in ids:assert readme.count(f'[{cid}](component_cards/{cid}.md)')==1,cid
assert '**Registered: 140 / 160' in readme
print('PASS: Waves 01-28; 140 unique IDs, 140 cards, evidence CSVs, single README table')
