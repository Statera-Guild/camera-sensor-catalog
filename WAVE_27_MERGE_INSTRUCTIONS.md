# Wave 27 — Camera Sensor Catalog

Adds CMP-CAM-0131 to CMP-CAM-0135 to the Wave 1–26 catalog. Requires existing `master_catalog_0001_0130.csv` and 130 component cards.

Run from repository root on Windows Anaconda Prompt:

```cmd
python APPLY_WAVE_27.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
```

Only if all three commands pass:

```cmd
git add .
git commit -m "Add Camera Sensor Catalog Wave 27 components 0131 to 0135"
git push origin main
git status
```

Expected: `Master created: 135 entries`, `README updated: 135 entries; single canonical table`, `PASS: Waves 01-27; 135 unique IDs, 135 cards, evidence CSVs, single README table`.

All five products are unverified editorial candidates, not manufacturer-qualified. Source URLs are manufacturer homepages only. Do not infer tested algorithm support or purchasing availability.
