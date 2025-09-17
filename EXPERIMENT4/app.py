from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import mean_squared_error

app = Flask(__name__)

# Load models
lr_model = joblib.load("backend/lr_model.pkl")
keras.losses.mse = keras.losses.mean_squared_error
lstm_model = load_model("backend/lstm_model.h5", compile=False)


@app.route('/')
def home():
    return render_template("index.html") 

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    days = int(data["days"])

    # Make predictions
    lr_pred = lr_model.predict(np.array([[days]]))
    lstm_pred = lstm_model.predict(np.array([[days]]))

    return jsonify({
        "lr_prediction": lr_pred.tolist(),
        "lstm_prediction": lstm_pred.tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)
