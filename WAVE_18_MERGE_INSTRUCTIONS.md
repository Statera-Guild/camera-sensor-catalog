# PAI-SG Camera Sensor Catalog — Wave 18

Prerequisite: clean local clone with Wave 17 committed (`master_catalog_0001_0085.csv`). Extract the ZIP into the repository root.

```cmd
cd /d C:\Users\abc\Downloads\camera-sensor-catalog
git status
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_18_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_18.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 18 components 0086 to 0090"
git push origin main
git status
```

Manufacturer homepage references are NOT verified product-level evidence. Model names, SKUs and claims remain `not_verified`; algorithm tests `not_tested`.
