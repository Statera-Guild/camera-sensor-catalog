# PAI-SG Camera Sensor Catalog — Wave 09

Scope: CMP-CAM-0041 through CMP-CAM-0045. Prerequisite: Wave 08 clean main branch, master_catalog_0001_0040.csv present.

Windows 10 Anaconda Prompt, run from C:\Users\abc\Downloads\camera-sensor-catalog:

```cmd
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_09_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_09.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 09 components 0041 to 0045"
git push origin main
git status
```

Do not treat unverified manufacturer URLs or candidate specifications as tested evidence. Inventory adds `product_form_factor`; master schema stays unchanged for compatibility.
