# Wave 13 Merge Instructions

Prerequisite: Wave 12 applied, validated, pushed; clean working tree. Extract ZIP into repository root (not a nested directory).

```cmd
cd /d C:\Users\abc\Downloads\camera-sensor-catalog
git status
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_13_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_13.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 13 components 0061 to 0065"
git push origin main
git status
```

Evidence: Manufacturer homepage reference only, model-specific claims not verified. Structural validation does not certify manufacturer claims.
