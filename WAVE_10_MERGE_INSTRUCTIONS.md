# Wave 10 — Merge instructions

Target: `Statera-Guild/camera-sensor-catalog`, Wave 10, CMP-CAM-0046 to CMP-CAM-0050.

1. Confirm clean `git status` in `C:\Users\abc\Downloads\camera-sensor-catalog`.
2. Extract `PAI_SG_Camera_Sensor_Catalog_Wave_10_20261010.zip` into the repository root, preserving paths.
3. Run `python APPLY_WAVE_10.py`, `python UPDATE_CAMERA_README_CATALOG.py`, and `python VALIDATE_CAMERA_CATALOG.py`.
4. Expected: 50 master rows, exactly one README Component Index table, all 50 cards, 10 evidence batches.
5. Commit and push only after validation PASS.

**Evidence note:** manufacturer URLs are homepage references, not verified product datasheets; all five records remain `not_verified` / `not_tested`. Do not promote their status without exact-SKU source checks.
