# CMP-CAM-0009 — Stereolabs ZED X One S Fisheye

- Manufacturer: Stereolabs
- Model: ZED X One S Fisheye
- Orderable SKU: ZED-414012
- Primary category: C06 — Fisheye / 360 Wide FoV
- Catalog status: **listed** (manufacturer listing only)
- Verification status: **not_verified**
- Algorithm test status: **not_tested**
- Manufacturer evidence: https://docs.stereolabs.com/docs/products/cameras/zedxone/specifications

## Manufacturer-source attributes (not hardware verified)

| Field | Value |
|---|---|
| output_type | RGB Frame / IMU |
| shutter_type | Global |
| resolution | 1920x1200 |
| fps | 60 at 1920x1200 |
| interface | GMSL2 |
| image_sensor | onsemi AR0234 RGB |

## Evidence notes

204 deg HFOV; fisheye SKU not IP69K; frame hardware synchronization supported

## Algorithm compatibility

Candidate inputs only: fisheye SLAM;visual odometry;surround perception;MOT. No SDK, ROS2, edge runtime, synchronization or algorithm integration tests were performed.

## Limitations

Manufacturer descriptions do not constitute independent qualification. Unknown fields remain not_verified; N/A only for inapplicable properties.
