"""2D Holographic Digital Twin Canvas Render Helpers"""
import cv2
import numpy as np

def create_blueprint_background(width: int = 640, height: int = 480, dark_mode: bool = True) -> np.ndarray:
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    bg_color = (15, 23, 42) if dark_mode else (248, 250, 252)
    canvas[:] = bg_color
    return canvas
