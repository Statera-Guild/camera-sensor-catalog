# Wave 03 merge (Windows 10 Anaconda Prompt)

Extract this ZIP into your existing camera-sensor-catalog repository, preserving folders. Then run:

```cmd
python APPLY_WAVE_03.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Add Camera Sensor Catalog Wave 03 components 0011 to 0015"
git push origin main
git status
```

The package intentionally does not contain README.md or prior master CSV files. Existing files are preserved. All Wave 03 technical specifications remain manufacturer claims, not hardware test results.
