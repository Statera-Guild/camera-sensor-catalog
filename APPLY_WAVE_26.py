from pathlib import Path
import csv
r=Path(__file__).resolve().parent
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:
  d=csv.DictReader(f);return d.fieldnames,list(d)
a=r/'validation_framework/integration/master_catalog_0001_0125.csv'
b=r/'validation_framework/wave_a/batch_0126_0130/wave26_master_rows.csv'
c=r/'validation_framework/integration/master_catalog_0001_0130.csv'
def assert_unique(rows,key):
 from collections import defaultdict
 d=defaultdict(list)
 for x in rows:d[(x['manufacturer'].strip().casefold(),x[key].strip().casefold())].append(x['component_id'])
 duplicates={k:v for k,v in d.items() if len(v)>1}
 if duplicates:raise ValueError(f'Duplicate {key}: {duplicates}')
fields,old=read(a);newfields,new=read(b)
assert fields==newfields
assert [x['component_id'] for x in old]==[f'CMP-CAM-{i:04d}' for i in range(1,126)]
assert [x['component_id'] for x in new]==[f'CMP-CAM-{i:04d}' for i in range(126,131)]
assert_unique(old+new,'model')
assert_unique(old+new,'orderable_sku')
for x in new:
 assert (r/'component_cards'/f"{x['component_id']}.md").exists()
 assert x['manufacturer_evidence_url'].startswith('https://')
if c.exists():
 _,existing=read(c)
 assert existing==old+new,'Refusing to overwrite different master'
 print('Master already correct: 130 entries')
else:
 with c.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(old+new)
 print('Master created: 130 entries')
