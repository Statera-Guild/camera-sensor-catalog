# Wave 12 Merge Instructions

Prerequisite: Wave 11 merged and `git status` clean; latest master `master_catalog_0001_0055.csv`. Extract ZIP directly into repository root (not a nested folder).

```cmd
cd /d C:\Users\abc\Downloads\camera-sensor-catalog
git status
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_12_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_12.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 12 components 0056 to 0060"
git push origin main
git status
```

Expected: `Master created: 60 entries`, `README updated: 60 entries; single canonical table`, and `PASS: Waves 01-12; 60 unique IDs, 60 cards, evidence CSVs, single README table`.

All model identity and specification fields remain **not_verified** until manufacturer-specific documentation is reviewed.
