# Camera Sensor Catalog — Wave 02 Integration

Baseline: Wave 01 commit 98a47b9 on main. Do not use this archive on an unrelated repository.

1. Extract ZIP into the existing `camera-sensor-catalog` directory, preserving subfolders.
2. `python APPLY_WAVE_02.py`
3. `python UPDATE_CAMERA_README_CATALOG.py`
4. `python VALIDATE_CAMERA_CATALOG.py`
5. `git add .` then commit/push/status.

Do not delete temporary files until push succeeds and working tree is clean. All claims are manufacturer-derived, not independent tests.
