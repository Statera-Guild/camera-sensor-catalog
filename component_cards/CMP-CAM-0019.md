# CMP-CAM-0019 — MicaSense RedEdge-P

- Manufacturer: MicaSense
- Model: RedEdge-P
- Orderable SKU: RedEdge-P (exact orderable SKU not_verified)
- Primary category: C14 — Multispectral/Hyperspectral
- Catalog status: **listed** (manufacturer listing only)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**
- Manufacturer evidence: https://support.micasense.com/hc/en-us/articles/4410824602903-RedEdge-P-Integration-Guide

## Source-backed manufacturer claims (not independently verified)

| Field | Manufacturer claim or qualification |
|---|---|
| output_type | 5 multispectral bands + panchromatic |
| shutter_type | Global |
| resolution | 1456x1088 per spectral band; 2464x2056 pan |
| fps | up to 3 captures/s (not video FPS) |
| interface | Ethernet / serial / GPIO |
| image_sensor | 5-band multispectral + panchromatic imagers |

## Candidate algorithms (not tested)

multispectral segmentation;vegetation indices;spectral anomaly

## Evidence limitations

RedEdge-P is multispectral with separate panchromatic imager; do not mislabel as hyperspectral. Capture rate is not conventional video FPS.

Manufacturer listing is not evidence of hardware testing, ROS2 integration, calibration quality, accuracy, safety certification, or current commercial availability. Public-only data; no private BOM, supplier agreements, or internal architecture.
