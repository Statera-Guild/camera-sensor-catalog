from pathlib import Path
import csv
r=Path(__file__).resolve().parent
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
rows=read(r/'validation_framework/integration/master_catalog_0001_0015.csv')
ids=[x['component_id'] for x in rows]
assert ids==[f'CMP-CAM-{i:04d}' for i in range(1,16)]
assert len({(x['manufacturer'].casefold(),x['orderable_sku'].casefold()) for x in rows})==15
for x in rows:
 assert (r/'component_cards'/f"{x['component_id']}.md").exists()
 assert x['manufacturer_evidence_url'].startswith('https://')
for a,b in [(1,5),(6,10),(11,15)]:
 d=r/f'validation_framework/wave_a/batch_{a:04d}_{b:04d}'
 for name in ['inventory.csv','source_registry.csv','specification_claims.csv','manufacturer_evidence_claims.csv','algorithm_compatibility.csv']:
  assert (d/name).exists(),str(d/name)
 assert [x['component_id'] for x in read(d/'inventory.csv')]==[f'CMP-CAM-{i:04d}' for i in range(a,b+1)]
readme=(r/'README.md').read_text(encoding='utf-8')
for cid in ids:assert f'[{cid}](component_cards/{cid}.md)' in readme,cid
print('PASS: Waves 01-03; 15 unique IDs, 15 cards, evidence CSVs, README')
