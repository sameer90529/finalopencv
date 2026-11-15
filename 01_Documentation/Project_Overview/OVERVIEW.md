# VisionDNA: Project Overview

## 1. Executive Summary
**VisionDNA** is an advanced AI computer vision and biomechanical analysis framework designed to construct and maintain a real-time, synchronized **Visual Digital Twin** of monitored individuals. Operating on standard commodity hardware (CPU or GPU), VisionDNA processes live camera feeds, classifies human motion states, forecasts near-future spatial trajectories and activity transitions, and continuously evaluates multidimensional safety risks.

## 2. Core Capabilities
- **Single-Pass Neural Perception**: Combines person localization and 17 full-body COCO keypoint estimation using YOLOv8-Pose in a unified, low-latency inference loop.
- **Biomechanical Kinematics**: Computes spine vertical angle deviation, knee/hip joint flexion, and bounding box aspect ratios to classify 6+ human activities (Standing, Walking, Sitting, Running, Bending, Falling).
- **Persistent Multi-Entity Tracking**: Retains track IDs with jitter-dampening deadband filtering, speed estimation (m/s proxy), and direction vectors.
- **Markovian Activity & Trajectory Forecasting**: Predicts next motion states using empirical transition matrices and extrapolates spatial trajectories 1.0s into the future.
- **Autonomous Multi-Factor Risk Engine**: Evaluates fall hazards, polygon restricted danger zones, abnormal speed, and inter-person collision proximity on a 0–100 scale.
- **2D Holographic Digital Twin Canvas**: Renders high-definition avatars on blueprint canvases with joint callouts, radar rings, and telemetry overlays.

## 3. Technology Stack
| Layer | Technologies |
|---|---|
| **Core AI & Models** | PyTorch, Ultralytics YOLOv8-Pose, OpenCV DNN, ONNX Runtime |
| **Computer Vision** | OpenCV 4.8+, Haar Cascades, NumPy |
| **Web Dashboard** | Streamlit, Pandas, Altair |
| **Hardware Interfacing** | PySerial, Arduino C++ Microcontroller Code |
| **Configuration** | PyYAML, TOML |
