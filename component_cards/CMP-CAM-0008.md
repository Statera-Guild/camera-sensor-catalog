# CMP-CAM-0008 — Luxonis OAK 4 D Pro

- Manufacturer: Luxonis
- Model: OAK 4 D Pro
- Orderable SKU: OAK 4 D Pro / variant SKU not_verified
- Primary category: C08 — Embedded AI Vision Camera
- Catalog status: **listed** (manufacturer listing only)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**
- Manufacturer evidence: https://docs.luxonis.com/hardware/products/OAK%204%20D%20Pro

## Manufacturer-source attributes (not hardware verified)

| Field | Value |
|---|---|
| output_type | RGB / Stereo IR / Depth / AI Metadata |
| shutter_type | Global (stereo IR); Rolling (RGB) |
| resolution | not_verified (per-output mode) |
| fps | not_verified (per-output mode) |
| interface | USB 2/3 or 2.5GbE (variant-dependent) |
| image_sensor | OV9282 x2 + Sony IMX586 RGB |

## Evidence notes

RVC4; IR projector; IMU; FSYNC/STROBE via M8; ROS2 not_tested

## Algorithm compatibility

Candidate inputs only: stereo depth;object detection;segmentation;MOT;edge AI. No SDK, ROS2, edge runtime, synchronization or algorithm integration tests were performed.

## Limitations

Manufacturer descriptions do not constitute independent qualification. Unknown fields remain not_verified; N/A only for inapplicable properties.
