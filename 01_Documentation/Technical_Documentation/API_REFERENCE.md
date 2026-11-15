# VisionDNA API Reference

## Module: `02_Source_Code.camera.camera_stream`
### `VideoStream(source=0, width=640, height=480, fps_limit=30, use_directshow=True)`
- `read() -> Tuple[bool, Optional[np.ndarray]]`: Returns `(success, frame)`.
- `seek_frame(frame_idx: int) -> bool`: Jump to target frame in video file.
- `draw_hud(frame, title, subtitle) -> np.ndarray`: Render top status HUD banner.
- `release()`: Closes video streams and hardware devices.

## Module: `02_Source_Code.detection.yolo_detector`
### `UnifiedPersonPoseDetector(model_path, confidence_threshold=0.35, device='cpu')`
- `detect_and_estimate(frame, inference_size=480) -> List[PersonDetection]`
- `draw_skeleton(frame, pose_res) -> np.ndarray`
- `draw_detections(frame, detections) -> np.ndarray`

## Module: `02_Source_Code.tracking.person_tracker`
### `PersonTracker(max_disappeared=15, max_distance=110.0, history_len=25, jitter_deadzone_px=2.0)`
- `update(detections: List[PersonDetection]) -> List[TrackedPerson]`
- `draw_tracks(frame, tracks) -> np.ndarray`

## Module: `02_Source_Code.activity_recognition.activity_classifier`
### `ActivityClassifier(smoothing_window=5)`
- `classify(pose, person, frame_height=480) -> ActivityResult`

## Module: `02_Source_Code.prediction.trajectory_predictor`
### `ActivityPredictor()`
- `predict(track_id, current_activity, velocity, center, danger_zones=None) -> PredictionResult`

## Module: `02_Source_Code.risk_assessment.risk_engine`
### `RiskEngine(danger_zones=None, proximity_threshold_px=80.0, low_max=30.0, medium_max=60.0)`
- `assess(person, all_people, activity_res, prediction_res=None) -> RiskAssessment`
- `draw_zones(frame) -> np.ndarray`

## Module: `02_Source_Code.digital_twin.twin_engine`
### `DigitalTwinEngine()`
- `update_twin(person, activity_res, pose_res=None, risk_score=0.0, risk_level='LOW', ...) -> DigitalTwinState`
- `render_canvas(width=640, height=480, pose_res=None, theme_colors=None, danger_zones=None) -> np.ndarray`
