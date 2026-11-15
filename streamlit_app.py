"""
VisionDNA - Unified Streamlit Web Application Entrypoint
Compatible with Render, Streamlit Cloud, and local environments.
"""
import os
import sys
import runpy

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "02_Source_Code")
for p in [ROOT_DIR, SRC_DIR, os.path.join(ROOT_DIR, "src")]:
    if p not in sys.path:
        sys.path.insert(0, p)

# Execute primary dashboard
dashboard_path = os.path.join(ROOT_DIR, "12_Main_Application", "dashboard.py")
if not os.path.exists(dashboard_path):
    dashboard_path = os.path.join(ROOT_DIR, "dashboard", "dashboard.py")

runpy.run_path(dashboard_path, run_name="__main__")
