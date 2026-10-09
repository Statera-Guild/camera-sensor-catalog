# Wave 02 Evidence Review

All five products have manufacturer-hosted pages or specification documentation. Only manufacturer-source claims are recorded. Hardware verification and algorithm testing: not_verified / not_tested.

- CMP-CAM-0006 — Orbbec Gemini 335L: https://store.orbbec.com/products/gemini-335l; 95 mm baseline; IP65; hardware multi-camera sync connector; ROS2 not_tested
- CMP-CAM-0007 — Orbbec Femto Bolt: https://www.orbbec.com/products/tof-camera/femto-bolt/; 0.25-5.46 m mode-dependent range; trigger supported; 10-25 C indoor stated
- CMP-CAM-0008 — Luxonis OAK 4 D Pro: https://docs.luxonis.com/hardware/products/OAK%204%20D%20Pro; RVC4; IR projector; IMU; FSYNC/STROBE via M8; ROS2 not_tested
- CMP-CAM-0009 — Stereolabs ZED X One S Fisheye: https://docs.stereolabs.com/docs/products/cameras/zedxone/specifications; 204 deg HFOV; fisheye SKU not IP69K; frame hardware synchronization supported
- CMP-CAM-0010 — Stereolabs ZED X One 4K Wide: https://docs.stereolabs.com/docs/products/cameras/zedxone/specifications; 85 dB dynamic range; HDR-capable sensor description; actual HDR mode not_verified

Special cautions: Orbbec Femto Bolt ToF mode-dependent FPS and range; OAK 4 D Pro output modes and precise SKU unresolved; ZED X One S fisheye variant does not inherit wide-lens-only IP69K; ZED X One 4K dynamic range is not proof of an enabled HDR mode; PTP and ROS2 support are not independently verified.
