# VisionDNA: AI-Based Visual Digital Twin for Predictive Human Activity and Risk Analysis

VisionDNA is a state-of-the-art AI computer vision and biomechanical analysis system that maintains a real-time synchronized **Visual Digital Twin** of detected individuals, classifies human activity, forecasts future spatial trajectories and state transitions, and conducts multi-condition autonomous safety risk evaluations.

---

## 🌐 Quick Access: Operations Dashboard & Apps

### 1. Launch Next-Gen Web Dashboard (Streamlit)
```bash
streamlit run 12_Main_Application/dashboard.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser.

### 2. Launch Standalone Desktop Operations Center (OpenCV)
```bash
python 12_Main_Application/app.py
```
*(Or run `python app.py` for root compatibility)*

#### ⌨️ Desktop App Hotkeys:
| Key | Action |
|---|---|
| `[TAB]` or `[M]` | Cycle View Mode: **Split Dual-View** ➔ **Perception Only** ➔ **Digital Twin** ➔ **PiP** |
| `[S]` | Toggle Biomechanical Skeleton Overlay |
| `[Z]` | Toggle Restricted Danger Zones |
| `[H]` | Toggle Sci-Fi Top HUD Banner |
| `[Q]` or `[ESC]` | Clean Shutdown |

### 3. Deploy to Render (Cloud Hosting)

This repository includes full automated configuration (`render.yaml`, `Dockerfile`, `Procfile`) for 1-click cloud deployment on [Render](https://render.com).

#### Option A: 1-Click Render Blueprint (Recommended)
1. Go to your [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** ➔ **Blueprint**.
3. Connect your repository: `https://github.com/sameer90529/finalopencv`.
4. Render will automatically detect `render.yaml` and configure the web service with:
   - **Build Command:** `pip install --upgrade pip && pip install -r requirements.txt`
   - **Start Command:** `streamlit run 12_Main_Application/dashboard.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`
5. Click **Apply** to deploy!

#### Option B: Manual Web Service Setup
1. In Render, click **New +** ➔ **Web Service**.
2. Select your repository `sameer90529/finalopencv`.
3. Set the following settings:
   - **Runtime:** `Python 3`
   - **Branch:** `main`
   - **Build Command:** `pip install --upgrade pip && pip install -r requirements.txt`
   - **Start Command:** `streamlit run 12_Main_Application/dashboard.py --server.port $PORT --server.address 0.0.0.0 --server.headless true`
   - **Environment Variable:** `PYTHON_VERSION` = `3.11.9`
4. Click **Create Web Service**.

---

```
VisionDNA/
├── 01_Documentation/             # Complete system & architecture documentation
│   ├── README.md                 # Primary documentation
│   ├── Project_Overview/         # Executive scope and technology stack
│   ├── System_Architecture/      # End-to-end dataflow and ASCII diagrams
│   └── Technical_Documentation/  # Mathematical formulas and API reference
├── 02_Source_Code/               # Modular core pipeline packages
│   ├── camera/                   # Video stream acquisition & synthetic test bench
│   ├── detection/                # Single-pass YOLOv8-Pose engine
│   ├── tracking/                 # Persistent multi-entity centroid tracking
│   ├── activity_recognition/     # Biomechanical motion state classification
│   ├── digital_twin/             # 2D holographic avatar canvas synchronizer
│   ├── prediction/               # Markovian transition & trajectory extrapolation
│   └── risk_assessment/          # Composite multi-condition safety risk engine
├── 03_AI_ML_Models/              # Deep neural network weights & manifests
│   ├── YOLO_Models/              # YOLOv8 object detector weights
│   ├── Pose_Models/              # YOLOv8-Pose 17-keypoint model weights
│   ├── Emotion_Models/           # FERPlus ONNX & FER2013 HDF5 models
│   └── Model_Configurations/     # Input dimensions and class manifests
├── 04_Computer_Vision/           # Vision utilities & Haar cascade detectors
│   ├── OpenCV/                   # OpenCV UI filters & Emotion inference
│   ├── Haar_Cascade/             # Frontal face cascade XML & detector
│   ├── Image_Processing/         # Tensor normalization & softmax transforms
│   └── Video_Processing/         # FPS counters & playback telemetry
├── 05_Dashboard/                 # Operations command center interface
│   ├── Streamlit/                # High-contrast interactive web app
│   ├── Components/               # Glassmorphism cards & HUD widgets
│   └── Visualizations/           # Blueprint viewports & metric plots
├── 06_Hardware/                  # Physical computing & edge integration
│   ├── Arduino/                  # C++ sketch for physical emotion LEDs
│   ├── Microcontroller_Code/     # PySerial controller with auto-reconnect
│   └── Hardware_Configuration/   # Wiring pinouts and baud parameters
├── 07_Configuration/             # Centralized YAML & TOML settings
│   ├── Application_Config/       # Primary system & Streamlit configs
│   ├── Camera_Config/            # Resolution & DirectShow settings
│   └── Model_Config/             # Confidence thresholds & tracking windows
├── 08_Datasets/                  # Data ingestion benchmarks & recordings
│   ├── Raw_Data/                 # Raw MP4/AVI surveillance feeds
│   ├── Processed_Data/           # Landmark logs & track histories
│   └── Sample_Data/              # Repeatable verification clips
├── 09_Testing/                   # Automated modular test suites
│   ├── Camera_Tests/             # Camera stream verification
│   ├── Detection_Tests/          # YOLOv8 & Haar face detector tests
│   ├── Pose_Tests/               # Keypoint extraction & skeleton tests
│   └── Integration_Tests/        # Complete end-to-end pipeline verification
├── 10_Assets/                    # Media & visual branding
│   ├── Images/                   # Architecture graphics & UI screenshots
│   ├── Icons/                    # Status indicators & radar symbols
│   └── UI_Assets/                # HUD styling and vector graphics
├── 11_Requirements/              # Python runtime dependencies
│   ├── requirements.txt          # Python package manifest
│   └── opencv.txt                # Core computer vision requirement tag
└── 12_Main_Application/          # Unified application entrypoints
    ├── app.py                    # Standalone desktop OpenCV runner
    └── dashboard.py              # Streamlit command center entrypoint
```

---

## 🧪 Automated Testing

Run the automated test suite from the repository root:

```bash
# 1. Test Camera Acquisition (Synthetic Mode)
python 09_Testing/Camera_Tests/test_camera_stream.py -1 5

# 2. Test YOLOv8 Person Detection
python 09_Testing/Detection_Tests/test_person_detector.py -1 5

# 3. Test YOLOv8-Pose Estimation
python 09_Testing/Pose_Tests/test_pose_estimator.py -1 5

# 4. Complete End-to-End Pipeline Verification
python 09_Testing/Integration_Tests/test_end_to_end_pipeline.py
```
