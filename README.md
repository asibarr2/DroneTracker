# Drone Detection with YOLOv8

A computer vision pipeline for detecting drones (UAVs) in images and video, built using the DUT Anti-UAV dataset and Ultralytics YOLOv8.

## Overview

This project trains a custom YOLOv8 object detection model to identify drones in aerial/surveillance footage, then runs inference on new images and video to detect and annotate drones in real time.

## Pipeline

1. **Label Conversion** (`convert.py`) — Converts Pascal VOC-style `.xml` annotations into YOLO-format `.txt` label files.
2. **Dataset Split** (`split.py`) — Splits images and labels into `train`/`val` sets and organizes them into the folder structure YOLOv8 expects.
3. **Training** — Fine-tunes a pretrained `yolov8n` model on the custom drone dataset using Ultralytics' CLI.
4. **Evaluation** — Reviews training/validation loss curves, precision/recall, and mAP metrics to assess model performance.
5. **Inference** — Runs the trained model on new images or video files to detect and draw bounding boxes around drones.

## Project Structure
├── convert.py              # XML → YOLO label conversion
├── split.py                # Train/val dataset split
├── detect_video.py         # Run detection on video files
├── data.yaml                # Dataset config for training
└── runs/                    # Training results & saved weights (gitignored)

## Setup

```bash
pip3 install ultralytics
```

## Usage

**1. Convert XML labels to YOLO format**
```bash
python3 convert.py
```

**2. Split into train/val folders**
```bash
python3 split.py
```

**3. Train the model**
```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=416 patience=15 device=mps
```

**4. Run detection on a video**
```bash
python3 detect_video.py
```

## Model

- **Base model:** YOLOv8n (nano) — chosen for faster training on CPU/Apple Silicon (MPS)
- **Classes:** `drone`
- **Dataset:** DUT Anti-UAV

## Results

_Add your training metrics here once finalized, e.g.:_
- mAP50: `X.XX`
- mAP50-95: `X.XX`
- Precision: `X.XX`
- Recall: `X.XX`

## Future Improvements

- Expand to multi-class detection (drone type/size)
- Real-time webcam/live feed support
- Alerting system on detection
