# Wave 03 Evidence Review

All claims are manufacturer-published, not independently verified. Hardware and algorithm tests are not performed.

- 0011: Astra 2 datasheet identifies model A30003-15; RGB rolling shutter differs from depth/IR global shutter.
- 0012: Basler product headline quotes 75 fps; actual default/throughput settings may yield different frame rate.
- 0013: Boson+ 22640A050 is a 50-degree lens configuration. Video interface options depend on selected module/integration; do not infer radiometric temperature measurement.
- 0014: Linea LA-GM-04K08A is a mono line-scan camera. 26 kHz is standard line rate, up to 80 kHz depends on TurboDrive; not an area-frame FPS.
- 0015: Basler a2A1920-160umBAS shares IMX392 family with Wave 1 model but is a distinct orderable USB3 SKU and 160-fps transport variant; catalog family-level deduplication policy should be reviewed.

No ROS2, PTP, Jetson, sensor accuracy, IP rating, or lifecycle support is claimed without specific verification.
