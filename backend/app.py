from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

print("🚀 Loading YOLOv8 model...")
model = YOLO("yolov8n.pt")
print("✅ Model loaded")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    image_bytes = file.read()
    image = Image.open(io.BytesIO(image_bytes))

    results = model(image)

    detections = []

    for result in results:
        boxes = result.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            detections.append({
                "bbox": [x1, y1, x2, y2],
                "confidence": round(conf, 2),
                "label": cls
            })

    return jsonify(detections)

if __name__ == "__main__":
    print("🚀 Starting Flask app...")
    app.run(host="0.0.0.0", port=5000)