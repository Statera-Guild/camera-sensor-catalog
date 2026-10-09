from pathlib import Path
import csv
root=Path(__file__).resolve().parent
p=root/'validation_framework/integration/master_catalog_0001_0005.csv'
with p.open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
ids=[r['component_id'] for r in rows]
assert ids==[f'CMP-CAM-{i:04d}' for i in range(1,6)], ids
assert len(set((r['manufacturer'].lower(),r['model'].lower()) for r in rows))==5
for r in rows:
 assert (root/'component_cards'/f"{r['component_id']}.md").is_file()
 assert r['manufacturer_evidence_url'].startswith('https://')
for name in ('source_registry.csv','specification_claims.csv','manufacturer_evidence_claims.csv','algorithm_compatibility.csv','inventory.csv'):
 assert (root/'validation_framework/wave_a/batch_0001_0005'/name).is_file()
print('PASS: Wave 01 5 unique IDs, 5 cards, evidence CSVs present')
