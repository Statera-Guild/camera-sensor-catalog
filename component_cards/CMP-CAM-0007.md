# CMP-CAM-0007 — Orbbec Femto Bolt

- Manufacturer: Orbbec
- Model: Femto Bolt
- Orderable SKU: Femto Bolt / orderable SKU not_verified
- Primary category: C05 — ToF Depth
- Catalog status: **listed** (manufacturer listing only)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**
- Manufacturer evidence: https://www.orbbec.com/products/tof-camera/femto-bolt/

## Manufacturer-source attributes (not hardware verified)

| Field | Value |
|---|---|
| output_type | RGB / IR / Depth / Point Cloud |
| shutter_type | N/A (ToF depth); RGB shutter not_verified |
| resolution | 640x576 NFOV depth |
| fps | 30 at 640x576 NFOV |
| interface | USB 3.2 Gen 1 Type-C |
| image_sensor | 850 nm ToF + RGB |

## Evidence notes

0.25-5.46 m mode-dependent range; trigger supported; 10-25 C indoor stated

## Algorithm compatibility

Candidate inputs only: depth estimation;3D perception;body tracking;robot manipulation. No SDK, ROS2, edge runtime, synchronization or algorithm integration tests were performed.

## Limitations

Manufacturer descriptions do not constitute independent qualification. Unknown fields remain not_verified; N/A only for inapplicable properties.
