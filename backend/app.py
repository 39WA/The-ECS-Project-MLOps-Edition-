from flask import Flask, request, jsonify
from ultralytics import YOLO
from PIL import Image
from flask_cors import CORS

print("🚀 Starting Flask app...")

app = Flask(__name__)
CORS(app)

model = None

@app.before_request
def load_model():
    global model
    if model is None:
        print("📦 Loading YOLO model...")
        model = YOLO("yolov8n.pt")
        print("✅ Model loaded")

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/")
def home():
    return "OK"

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
    app.run(host="0.0.0.0", port=5000)