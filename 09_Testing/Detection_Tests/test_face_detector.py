"""
Stage 2: Face Detection Live Test Script
Tests real-time OpenCV Haar Cascade face detection on camera feed.
"""

import cv2
import time
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
for p in [ROOT_DIR, os.path.join(ROOT_DIR, "04_Computer_Vision", "Haar_Cascade")]:
    if p not in sys.path:
        sys.path.insert(0, p)
try:
    from face_detector import FaceDetector
except ImportError:
    from src.face_detection import FaceDetector


def run_face_detection_test(camera_index: int = 0):
    print("=" * 50)
    print("STAGE 2: FACE DETECTION LIVE TEST")
    print("=" * 50)

    try:
        detector = FaceDetector(cascade_path="04_Computer_Vision/Haar_Cascade/haarcascade_frontalface_default.xml")
        print("[SUCCESS] Haar Cascade Face Detector initialized.")
    except Exception as e:
        print(f"[ERROR] Failed to initialize FaceDetector: {e}")
        return False

    print(f"Opening camera index {camera_index}...")
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print(f"[ERROR] Unable to access camera at index {camera_index}.")
        return False

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    window_name = "Stage 2 - Face Detection (Press Q to Exit)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    prev_time = time.time()
    fps = 0.0

    print("Camera feed active. Point camera at your face.")
    print("Press 'q' or 'ESC' to exit.\n")

    try:
        while True:
            ret, frame = cap.read()
            if not ret or frame is None:
                continue

            curr_time = time.time()
            dt = curr_time - prev_time
            if dt > 0:
                fps = 0.9 * fps + 0.1 * (1.0 / dt) if fps > 0 else (1.0 / dt)
            prev_time = curr_time

            faces = detector.detect_faces(frame)

            for bbox in faces:
                frame = detector.draw_face_annotations(
                    frame, bbox, label="Face Detected", confidence=100.0, show_label=True
                )

            cv2.imshow(window_name, frame)
            key = cv2.waitKey(1) & 0xFF
            if key in [ord('q'), ord('Q'), 27]:
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

    return True


if __name__ == "__main__":
    cam_idx = 0
    if len(sys.argv) > 1:
        try:
            cam_idx = int(sys.argv[1])
        except ValueError:
            cam_idx = 0
    run_face_detection_test(camera_index=cam_idx)
