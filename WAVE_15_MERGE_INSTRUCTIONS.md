# PAI-SG Camera Sensor Catalog — Wave 15

## Prerequisites

Run in a clean local clone containing committed Wave 14 (master_catalog_0001_0070.csv). Unzip this package into the repository root, preserving folders.

## Windows Anaconda Prompt

```cmd
cd /d C:\Users\abc\Downloads\camera-sensor-catalog
git status
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_15_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_15.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 15 components 0071 to 0075"
git push origin main
git status
```

Manufacturer homepage references are NOT manufacturer-verified model-specific evidence. All new product claims remain not_verified and algorithm tests not_tested.
