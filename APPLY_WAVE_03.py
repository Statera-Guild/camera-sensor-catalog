from pathlib import Path
import csv
r=Path(__file__).resolve().parent
def load(p):
 with p.open(encoding='utf-8-sig',newline='') as f:
  d=csv.DictReader(f);return d.fieldnames,list(d)
a=r/'validation_framework/integration/master_catalog_0001_0010.csv'
b=r/'validation_framework/wave_a/batch_0011_0015/wave03_master_rows.csv'
c=r/'validation_framework/integration/master_catalog_0001_0015.csv'
if not a.exists():raise SystemExit('ERROR: missing Wave 2 master')
fields,old=load(a);new_fields,new=load(b)
assert fields==new_fields
assert [x['component_id'] for x in old]==[f'CMP-CAM-{i:04d}' for i in range(1,11)]
assert [x['component_id'] for x in new]==[f'CMP-CAM-{i:04d}' for i in range(11,16)]
assert len({(x['manufacturer'].casefold(),x['orderable_sku'].casefold()) for x in old+new})==15
for x in new:
 assert (r/'component_cards'/f"{x['component_id']}.md").exists()
 assert x['manufacturer_evidence_url'].startswith('https://')
if c.exists():
 _,existing=load(c)
 if existing!=old+new:raise SystemExit('ERROR: existing master differs; refusing overwrite')
 print('Master already correct: 15 entries')
else:
 with c.open('w',encoding='utf-8',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(old+new)
 print('Master created: 15 entries')
