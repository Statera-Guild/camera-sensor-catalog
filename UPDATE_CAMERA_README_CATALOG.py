from pathlib import Path
import csv
root=Path(__file__).resolve().parent
master=root/'validation_framework/integration/master_catalog_0001_0010.csv'
if not master.is_file():raise SystemExit('Run APPLY_WAVE_02.py first')
with master.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
readme=root/'README.md';s=readme.read_text(encoding='utf-8')
a='<!-- PAI-SG-CAMERA-CATALOG:START -->';b='<!-- PAI-SG-CAMERA-CATALOG:END -->'
assert a in s and b in s and s.index(a)<s.index(b)
lines=['## Component Index','','**Registered: 10 / 160 (6.25%) · Waves 1–2**','','| Component ID | Manufacturer | Model | Status | Verification | Algorithm Test |','|---|---|---|---|---|---|']
for r in rows:
 c=r['component_id'];lines.append(f"| [{c}](component_cards/{c}.md) | {r['manufacturer']} | {r['model']} | listed | not_verified | not_tested |")
s=s[:s.index(a)+len(a)]+'\n'+'\n'.join(lines)+'\n'+s[s.index(b):]
readme.write_text(s,encoding='utf-8')
print('README updated:',len(rows),'entries')
