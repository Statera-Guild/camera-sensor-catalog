# Wave 08 — Windows Anaconda Prompt

Extract the ZIP directly into the existing `camera-sensor-catalog` repository root. Ensure `git status` is clean before applying.

```cmd
cd /d C:\Users\abc\Downloads\camera-sensor-catalog
git status
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'C:\Users\abc\Downloads\PAI_SG_Camera_Sensor_Catalog_Wave_08_20261010.zip' -DestinationPath 'C:\Users\abc\Downloads\camera-sensor-catalog' -Force"
python APPLY_WAVE_08.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 08 components 0036 to 0040"
git push origin main
git status
```

Expected: 40 entries, one README Component Index table. Manufacturer evidence remains unverified.
