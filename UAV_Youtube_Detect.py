from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

results = model.predict(
    source="/Users/rinzler/Desktop/Code_Practice/DroneTracker/drone_flying.mp4",
    save=True,
    show=True,
    conf=0.4
)