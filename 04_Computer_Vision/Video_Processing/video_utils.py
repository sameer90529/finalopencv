"""Video Processing and Telemetry Helpers"""
import time

class FPSTracker:
    def __init__(self, alpha: float = 0.9):
        self.alpha = alpha
        self.fps = 0.0
        self.prev_time = time.time()

    def update(self) -> float:
        curr = time.time()
        dt = curr - self.prev_time
        if dt > 0:
            instant = 1.0 / dt
            self.fps = self.alpha * self.fps + (1.0 - self.alpha) * instant if self.fps > 0 else instant
        self.prev_time = curr
        return self.fps
