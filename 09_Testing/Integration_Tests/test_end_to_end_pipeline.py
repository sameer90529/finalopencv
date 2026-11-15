"""
VisionDNA - Complete End-to-End Pipeline Integration Test
Verifies: VideoStream -> UnifiedPersonPoseDetector -> PersonTracker ->
ActivityClassifier -> ActivityPredictor -> RiskEngine -> DigitalTwinEngine
"""

import os
import sys
import time
import numpy as np

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(ROOT_DIR, "02_Source_Code")
for p in [ROOT_DIR, SRC_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

from camera.camera_stream import VideoStream
from detection.yolo_detector import UnifiedPersonPoseDetector
from tracking.person_tracker import PersonTracker
from activity_recognition.activity_classifier import ActivityClassifier
from prediction.trajectory_predictor import ActivityPredictor
from risk_assessment.risk_engine import RiskEngine
from digital_twin.twin_engine import DigitalTwinEngine


def run_e2e_test(num_frames: int = 5):
    print("=" * 70)
    print("VISIONDNA: COMPLETE END-TO-END PIPELINE INTEGRATION TEST")
    print("=" * 70)

    # 1. Initialize Pipeline Modules
    print("[1/7] Initializing VideoStream (Synthetic Mode)...")
    stream = VideoStream(source=-1, width=640, height=480)
    assert stream.is_opened, "VideoStream failed to initialize!"
    print("      PASS: VideoStream operational.")

    print("[2/7] Initializing YOLOv8-Pose Unified Detector...")
    detector = UnifiedPersonPoseDetector(
        model_path="03_AI_ML_Models/Pose_Models/yolov8n-pose.pt",
        confidence_threshold=0.35,
    )
    print("      PASS: Detector initialized.")

    print("[3/7] Initializing PersonTracker...")
    tracker = PersonTracker()
    print("      PASS: Tracker initialized.")

    print("[4/7] Initializing ActivityClassifier...")
    activity_classifier = ActivityClassifier()
    print("      PASS: ActivityClassifier initialized.")

    print("[5/7] Initializing ActivityPredictor & Trajectory Engine...")
    predictor = ActivityPredictor()
    print("      PASS: ActivityPredictor initialized.")

    print("[6/7] Initializing RiskEngine & Danger Zones...")
    risk_engine = RiskEngine()
    print("      PASS: RiskEngine initialized.")

    print("[7/7] Initializing DigitalTwinEngine...")
    digital_twin = DigitalTwinEngine()
    print("      PASS: DigitalTwinEngine initialized.")

    print("\nRunning live frame synchronization cycle...")
    for f in range(num_frames):
        ret, frame = stream.read()
        assert ret and frame is not None, f"Frame {f+1} capture failed!"

        detections = detector.detect_and_estimate(frame)
        tracks = tracker.update(detections)

        active_pose = None
        for p in tracks:
            act_res = activity_classifier.classify(p.pose, p, frame_height=480)
            pred_res = predictor.predict(p.track_id, act_res.activity, p.velocity, p.center)
            risk_res = risk_engine.assess(p, tracks, act_res, pred_res)
            digital_twin.update_twin(p, act_res, p.pose, risk_res.risk_score, risk_res.risk_level)
            if p.pose and p.pose.is_valid:
                active_pose = p.pose

        canvas = digital_twin.render_canvas(width=640, height=480, pose_res=active_pose)
        assert canvas.shape == (480, 640, 3), "Invalid canvas shape!"
        print(f"  Frame {f+1}/{num_frames}: Processed {len(tracks)} tracks | Canvas Rendered: {canvas.shape}")

    stream.release()
    print("\n" + "=" * 70)
    print("[E2E TEST PASS] ALL 7 PIPELINE MODULES SYNCHRONIZED SUCCESSFULLY!")
    print("=" * 70 + "\n")
    return True


if __name__ == "__main__":
    run_e2e_test(5)
