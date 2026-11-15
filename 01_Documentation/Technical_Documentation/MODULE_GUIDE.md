# VisionDNA Technical Module Guide

### 1. Camera Acquisition (`02_Source_Code/camera/camera_stream.py`)
- **Class**: `VideoStream`
- **Capabilities**: Windows DirectShow (`cv2.CAP_DSHOW`) fallback for zero-latency camera binding; video looping; frame seeking; and built-in synthetic test generation (`source=-1`).

### 2. Detection & Pose (`02_Source_Code/detection/yolo_detector.py`)
- **Class**: `UnifiedPersonPoseDetector`
- **Inference**: Single-pass YOLOv8-Pose CPU execution at 480x480 resolution.
- **Keypoints**: 17 COCO landmarks (nose, eyes, ears, shoulders, elbows, wrists, hips, knees, ankles).
- **Formulas**:
  - **Spine Angle**: `arctan2(|dx|, |dy|)` between shoulder center and hip center relative to vertical.
  - **Joint Flexion**: Vector cosine formula `arccos((v1 . v2) / (|v1| * |v2|))` for knee, hip, and elbow articulation.

### 3. Tracking (`02_Source_Code/tracking/person_tracker.py`)
- **Class**: `PersonTracker`
- **Logic**: Euclidean centroid matching with deadzone thresholding (2.0 px) to eliminate camera jitter. Computes directional vectors and maintains a 25-frame history deque.

### 4. Activity Classification (`02_Source_Code/activity_recognition/activity_classifier.py`)
- **Class**: `ActivityClassifier`
- **Categories**: Standing, Walking, Sitting, Running, Bending, Falling, Gesturing.
- **Heuristics**:
  - **Fall**: `spine_angle > 55 deg` AND `aspect_ratio < 0.9` AND rapid downward vertical translation.
  - **Sitting**: `knee_angle < 130 deg` AND `norm_top_y > 0.35`.
  - **Locomotion**: Velocity thresholds (`v >= 0.2 m/s` for Walking, `v >= 1.8 m/s` for Running).

### 5. Prediction Engine (`02_Source_Code/prediction/trajectory_predictor.py`)
- **Class**: `ActivityPredictor`
- **Markov Transition Matrix**: Discrete first-order probability transitions between activity states.
- **Spatial Extrapolation**: Linear velocity vector extrapolation: `(x + vx * dt, y + vy * dt)` for `dt = 1.0s`.

### 6. Risk Engine (`02_Source_Code/risk_assessment/risk_engine.py`)
- **Class**: `RiskEngine`
- **Assessment Components**:
  - Critical Fall Hazard: +50 score.
  - Restricted Polygon Intrusion (`cv2.pointPolygonTest`): +45 score.
  - Velocity Anomaly: +20 score.
  - Multi-person Proximity Collision (`dist < 80px`): +25 score.

### 7. Digital Twin Engine (`02_Source_Code/digital_twin/twin_engine.py`)
- **Class**: `DigitalTwinEngine`
- **Rendering**: Generates holographic 2D humanoid avatars reflecting physical pose, range rings, crosshairs, and live telemetry cards.
