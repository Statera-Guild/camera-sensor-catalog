# Wave 20 Merge Instructions

Prerequisite: Waves 01–19 committed; working tree clean. Extract this ZIP at repository root.

```cmd
python APPLY_WAVE_20.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 20 components 0096 to 0100"
git push origin main
git status
```

Expected: master 100, README 100, PASS Waves 01-20. All five new records remain not_verified/not_tested; homepage URLs are not model-specific evidence.
