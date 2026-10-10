# Wave 25 — Camera Sensor Catalog

Adds CMP-CAM-0121 to CMP-CAM-0125 to Wave 1–24 catalog. Requires existing `master_catalog_0001_0120.csv` and 120 component cards.

Run from repository root on Windows Anaconda Prompt:

```cmd
python APPLY_WAVE_25.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 25 components 0121 to 0125"
git push origin main
git status
```

Expected: `Master created: 125 entries`, `README updated: 125 entries; single canonical table`, `PASS: Waves 01-25; 125 unique IDs, 125 cards, evidence CSVs, single README table`.

All five products are unverified editorial candidates, not manufacturer-qualified. Source URLs are manufacturer homepages only. Do not infer tested algorithm support or purchasing availability.
