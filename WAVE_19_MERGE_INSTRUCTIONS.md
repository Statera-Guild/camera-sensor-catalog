# PAI-SG Camera Sensor Catalog — Wave 19

## Prerequisites

Run in a clean local clone containing committed Wave 18 (`master_catalog_0001_0090.csv`). Unzip this package into the repository root, preserving folders.

## Windows Anaconda Prompt

```cmd
cd /d C:\Users\abc\Downloads\camera-sensor-catalog
git status
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_19_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_19.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 19 components 0091 to 0095"
git push origin main
git status
```

Manufacturer homepage references are NOT manufacturer-verified model-specific evidence. All new product claims remain `not_verified` and algorithm tests `not_tested`.
