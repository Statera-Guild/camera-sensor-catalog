# Wave 25 corrective overlay (after commit ca6e84b)

This overlay replaces four duplicate candidates in Wave 25 only; existing 1-120 entries remain unchanged.

- CMP-CAM-0121: Teledyne FLIR A70 (replaces duplicate A50)
- CMP-CAM-0122: Orbbec Gemini 335 (replaces duplicate Femto Mega)
- CMP-CAM-0123: Zivid Zivid 2+ L110 (unchanged)
- CMP-CAM-0124: MicaSense RedEdge-MX (replaces duplicate RedEdge-P)
- CMP-CAM-0125: Luxonis OAK-D Lite (replaces duplicate OAK-FFC 4P)

Product model/SKU claims are candidate records only and not manufacturer-verified. No exact SKU validation or algorithm testing has been performed.

Unzip into repository with overwrite, then run:

```cmd
python APPLY_WAVE_25.py
python UPDATE_CAMERA_README_CATALOG.py
python VALIDATE_CAMERA_CATALOG.py
git add .
git commit -m "Fix Wave 25 duplicate camera models and integrate 125 entries"
git push origin main
git status
```

Expected PASS: Waves 01-25; 125 unique IDs, 125 cards, evidence CSVs, single README table.
