from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image

print("🚀 Starting Flask app...")

app = Flask(__name__)

model = YOLO("yolov8n.pt")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    image = Image.open(file.stream)

    results = model(image)

    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "label": int(box.cls[0]),
                "confidence": float(box.conf[0]),
                "bbox": box.xyxy[0].tolist()
            })

    return jsonify(detections)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)