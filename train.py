from ultralytics import YOLO

MODEL_PATH = 'yolov8n.pt'
model = YOLO(MODEL_PATH)

YAMEL_PATH = 'data/data.yaml'
EPOCHS = 45
IMG_SIZE = 320
BATCH_SIZE = 2

model.train(data=YAMEL_PATH,
            epochs=EPOCHS,
            imgsz=IMG_SIZE,
            batch=BATCH_SIZE)
