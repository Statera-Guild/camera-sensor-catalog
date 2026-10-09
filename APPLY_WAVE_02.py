from pathlib import Path
import csv
root=Path(__file__).resolve().parent
base=root/'validation_framework/integration'
old=base/'master_catalog_0001_0005.csv'
new=base/'master_catalog_0001_0010.csv'
inc=root/'validation_framework/wave_a/batch_0006_0010/inventory.csv'
def read(p):
 if not p.is_file():raise SystemExit('ERROR missing '+str(p))
 with p.open(encoding='utf-8-sig',newline='') as f:r=csv.DictReader(f);return r.fieldnames,list(r)
fields,prior=read(old)
_,incoming=read(inc)
expected_prior=[f'CMP-CAM-{i:04d}' for i in range(1,6)]
expected_new=[f'CMP-CAM-{i:04d}' for i in range(6,11)]
if [r['component_id'] for r in prior]!=expected_prior:raise SystemExit('ERROR Wave 1 baseline changed')
if [r['component_id'] for r in incoming]!=expected_new:raise SystemExit('ERROR Wave 2 inventory IDs invalid')
for r in incoming:
 if not (root/'component_cards'/f"{r['component_id']}.md").is_file():raise SystemExit('ERROR missing card '+r['component_id'])
# extra columns retained only from Wave 1 schema; each wave inventory is canonical source of identifiers
from importlib.util import spec_from_file_location,module_from_spec
batch=root/'validation_framework/wave_a/batch_0006_0010'
extra=batch/'wave02_master_rows.csv'
extra_fields,add=read(extra)
if fields!=extra_fields or [r['component_id'] for r in add]!=expected_new:raise SystemExit('ERROR master schema or IDs mismatch')
for r in add:
 if not r['manufacturer_evidence_url'].startswith('https://'):raise SystemExit('ERROR evidence URL')
 if (r['manufacturer'].strip().lower(),r['model'].strip().lower()) in {(x['manufacturer'].strip().lower(),x['model'].strip().lower()) for x in prior}:raise SystemExit('ERROR duplicate model')
if new.exists():
 _,existing=read(new)
 if existing!=prior+add:raise SystemExit('ERROR existing master differs; no overwrite')
 print('Master already correct: 10 entries')
else:
 with new.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(prior+add)
 print('Master created: 10 entries')
