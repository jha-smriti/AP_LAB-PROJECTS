from flask import Flask, request, jsonify, render_template
import joblib
import cv2
import numpy as np

app = Flask(__name__)

# Load models
models = {
    "svm": joblib.load("svm_model.pkl"),
    "random_forest": joblib.load("rf_model.pkl"),
    "logistic_regression": joblib.load("lr_model.pkl"),
}

# Image preprocessing for uploads
def preprocess_uploaded_image(file, size=(64, 64)):
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, size)
    return image.flatten().reshape(1, -1)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]
    model_name = request.form.get("model", "svm")
    model = models.get(model_name)

    if model:
        image = preprocess_uploaded_image(file)
        prediction = model.predict(image)[0]
        label = "Dog" if prediction == 1 else "Cat"
        return jsonify({"prediction": label})
    
    return jsonify({"error": "Invalid model name"})

if __name__ == "__main__":
    app.run(debug=True)
