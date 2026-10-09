from pathlib import Path
import csv
r=Path(__file__).resolve().parent
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:
  d=csv.DictReader(f);return d.fieldnames,list(d)
a=r/'validation_framework/integration/master_catalog_0001_0045.csv'
b=r/'validation_framework/wave_a/batch_0046_0050/wave10_master_rows.csv'
c=r/'validation_framework/integration/master_catalog_0001_0050.csv'
fields,old=read(a);newfields,new=read(b)
assert fields==newfields
assert [x['component_id'] for x in old]==[f'CMP-CAM-{i:04d}' for i in range(1,46)]
assert [x['component_id'] for x in new]==[f'CMP-CAM-{i:04d}' for i in range(46,51)]
assert len({(x['manufacturer'].casefold(),x['model'].casefold()) for x in old+new})==50
assert len({(x['manufacturer'].casefold(),x['orderable_sku'].casefold()) for x in old+new})==50
for x in new:
 assert (r/'component_cards'/f"{x['component_id']}.md").exists()
 assert x['manufacturer_evidence_url'].startswith('https://')
if c.exists():
 _,existing=read(c)
 assert existing==old+new,'Refusing to overwrite different master'
 print('Master already correct: 50 entries')
else:
 with c.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(old+new)
 print('Master created: 50 entries')
