# Wave 11 Merge Instructions

Prerequisite: Wave 10 merged and `git status` clean; latest master `master_catalog_0001_0050.csv`. Extract ZIP directly into repository root (not a nested folder).

```cmd
cd /d C:\Users\abc\Downloads\camera-sensor-catalog
git status
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_11_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_11.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 11 components 0051 to 0055"
git push origin main
git status
```

Expected: `Master created: 55 entries`, `README updated: 55 entries; single canonical table`, and `PASS: Waves 01-11; 55 unique IDs, 55 cards, evidence CSVs, single README table`.

All model identity and specification fields remain **not_verified** until manufacturer-specific documentation is reviewed.
