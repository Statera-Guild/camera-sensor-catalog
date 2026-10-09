# PAI-SG Camera Sensor Catalog — Wave 14

Adds CMP-CAM-0066 through CMP-CAM-0070 to a clean Wave 13 checkout.

From `C:\Users\abc\Downloads\camera-sensor-catalog` run:

```cmd
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_14_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_14.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 14 components 0066 to 0070"
git push origin main
git status
```

No product-level manufacturer evidence was live-verified.
