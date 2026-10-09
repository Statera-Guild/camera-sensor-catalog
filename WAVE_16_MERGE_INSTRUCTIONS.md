# PAI-SG Camera Sensor Catalog — Wave 16

New component IDs: `CMP-CAM-0076`–`CMP-CAM-0080`. Extract ZIP into the repository root (not into a nested folder), then run:

```cmd
python APPLY_WAVE_16.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 16 components 0076 to 0080"
git push origin main
git status
```

Prerequisite: Wave 15 master `validation_framework/integration/master_catalog_0001_0075.csv` must exist. The apply script refuses conflicting output. Evidence is editorial and not independently manufacturer-verified.
