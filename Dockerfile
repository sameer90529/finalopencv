# ==============================================================================
# VisionDNA - Production Dockerfile for Render Deployment
# ==============================================================================
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# Install system dependencies for OpenCV and multimedia processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy repository source code
COPY . .

# Render dynamically sets $PORT at runtime
ENV PORT=8501
EXPOSE 8501

# Start Streamlit web application
CMD ["sh", "-c", "streamlit run 12_Main_Application/dashboard.py --server.port=${PORT:-8501} --server.address=0.0.0.0 --server.headless=true"]
