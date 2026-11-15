# VisionDNA: System Architecture

```text
                    +------------------------------------+
                    |        Visual Data Source          |
                    | (Webcam / Video File / Synthetic)  |
                    +-----------------+------------------+
                                      |
                                      v
                    +------------------------------------+
                    |  Unified Person & Pose Detector    |
                    |         (YOLOv8-Pose Engine)       |
                    +-----------------+------------------+
                                      | Bounding Boxes + 17 Keypoints
                                      v
                    +------------------------------------+
                    |       Persistent Tracker           |
                    |    (Centroid / Deadzone Filtering) |
                    +-----------------+------------------+
                                      | Track IDs + Velocity + Trajectory
                                      v
          +---------------------------+---------------------------+
          |                                                       |
          v                                                       v
+-------------------------------+                       +-------------------------------+
|    Biomechanical Activity     |                       |    Predictive Trajectory &    |
|          Classifier           |                       |      Markov State Engine      |
+-----------------+-------------+                       +-----------------+-------------+
                  | Activity + Joint Flexion                              | Next-State + Future (x, y)
                  +---------------------------+---------------------------+
                                              |
                                              v
                              +-------------------------------+
                              |    Multi-Condition Safety     |
                              |         Risk Engine           |
                              | (Falls / Zones / Proximity)   |
                              +---------------+---------------+
                                              | Composite Risk (0-100)
                                              v
                              +-------------------------------+
                              |     Digital Twin Engine       |
                              |   (Real-Time Synchronizer)    |
                              +---------------+---------------+
                                              |
                      +-----------------------+-----------------------+
                      |                                               |
                      v                                               v
        +-----------------------------+                 +-----------------------------+
        |   Streamlit Operations HUD  |                 | Standalone OpenCV Viewport  |
        |    (12_Main_Application/    |                 |    (12_Main_Application/    |
        |        dashboard.py)        |                 |           app.py)           |
        +-----------------------------+                 +-----------------------------+
```

## Dataflow Pipeline Specifications

1. **Acquisition Stage**: Captures RGB frames (640x480 standard) via OpenCV DirectShow, MP4 file playback, or synthetic generator.
2. **Inference Stage**: YOLOv8-Pose performs single-pass bounding box and 17 keypoint regression.
3. **Tracking Stage**: Multi-object tracker matches Euclidean distance centroids within a 110px radius and maintains persistent entity lifecycles.
4. **Kinematic Stage**: Computes torso vertical alignment angle and joint flexion (knee and hip).
5. **Prediction Stage**: Applies a 6x6 Markov state transition matrix to forecast likely next activity alongside velocity vector extrapolation.
6. **Risk Assessment Stage**: Checks bounding box intersections against polygon danger zones and flags fall postures or proximity breaches.
7. **Digital Twin Stage**: Synchronizes real-world kinematic state with holographic 2D avatar blueprint canvas.
