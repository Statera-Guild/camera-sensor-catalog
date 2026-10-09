from pathlib import Path
import csv
root=Path(__file__).resolve().parent
base=root/'validation_framework/integration/master_catalog_0001_0010.csv'
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
rows=read(base)
ids=[r['component_id'] for r in rows]
assert ids==[f'CMP-CAM-{i:04d}' for i in range(1,11)],ids
assert len({(r['manufacturer'].strip().casefold(),r['model'].strip().casefold()) for r in rows})==10
for r in rows:
 assert (root/'component_cards'/f"{r['component_id']}.md").is_file()
 assert r['manufacturer_evidence_url'].startswith('https://')
for a,b in [(1,5),(6,10)]:
 d=root/f'validation_framework/wave_a/batch_{a:04d}_{b:04d}'
 for n in ('inventory.csv','source_registry.csv','specification_claims.csv','manufacturer_evidence_claims.csv','algorithm_compatibility.csv'):
  assert (d/n).is_file(),str(d/n)
 assert [x['component_id'] for x in read(d/'inventory.csv')]==[f'CMP-CAM-{i:04d}' for i in range(a,b+1)]
readme=(root/'README.md').read_text(encoding='utf-8')
for id in ids:assert f'[{id}](component_cards/{id}.md)' in readme,id
print('PASS: Waves 01-02; 10 unique IDs, 10 cards, evidence CSVs, README')
