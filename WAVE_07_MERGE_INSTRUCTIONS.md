# Camera Sensor Catalog Wave 07 (CMP-CAM-0031–0035)

Unzip at repository root; do not delete previous master catalogs.

```cmd
python APPLY_WAVE_07.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 07 components 0031 to 0035"
git push origin main
git status
```

Expected: 35 master rows and exactly one README Component Index table. Source URLs and SKU-specific claims are not live-verified; no hardware testing performed.
