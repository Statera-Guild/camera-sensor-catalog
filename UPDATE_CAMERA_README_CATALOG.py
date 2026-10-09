from pathlib import Path
import csv,re
r=Path(__file__).resolve().parent
files=sorted((r/'validation_framework/integration').glob('master_catalog_*.csv'))
if not files:raise SystemExit('ERROR: no master')
with files[-1].open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
readme=r/'README.md'
text=readme.read_text(encoding='utf-8') if readme.exists() else '# PAI-SG Camera Sensor Catalog\n'
start='<!-- CAMERA_CATALOG_START -->';end='<!-- CAMERA_CATALOG_END -->'
section='\n'.join(f"- [{x['component_id']}](component_cards/{x['component_id']}.md) — {x['manufacturer']} {x['model']}" for x in rows)
if start in text and end in text:
 text=text[:text.index(start)]+start+'\n'+section+'\n'+end+text[text.index(end)+len(end):]
else:
 # Preserve historical README content and append a new canonical index.
 text=text.rstrip()+'\n\n## Component index\n'+start+'\n'+section+'\n'+end+'\n'
readme.write_text(text,encoding='utf-8')
print(f'README updated: {len(rows)} entries')
