"""
Day 1: Real-time object detection on your webcam using YOLOv8.

Setup (run once in Terminal):
    pip install ultralytics opencv-python

Run:
    python3 day1_webcam_detect.py

Press 'q' to quit.
"""

from ultralytics import YOLO
import cv2

# Loads a small pretrained model automatically on first run (~6MB download)
model = YOLO("yolov8n.pt")

# 0 = default webcam. If you have multiple cameras, try 1, 2, etc.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open webcam. Check Mac camera permissions for Terminal/your IDE.")

print("Webcam running. Press 'q' in the video window to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection on the current frame
    results = model.track(frame, persist=True)

    # results[0].plot() draws boxes + labels for you
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
