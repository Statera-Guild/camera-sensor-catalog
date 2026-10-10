# Wave 26 Merge Instructions

Extract ZIP into the root of `camera-sensor-catalog` (do not create an extra enclosing folder). From repository root run:

```cmd
python APPLY_WAVE_26.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
```

Commit and push **only after PASS**. These five catalog candidates are **not manufacturer verified**; no exact SKU, product availability, or algorithm test is asserted.
