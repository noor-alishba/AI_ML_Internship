from flask import Flask, jsonify, request
import joblib
import pandas as pd
import logging
import os
import json
from datetime import datetime

app = Flask(__name__)

# Create logs directory if it does not exist
os.makedirs("logs", exist_ok=True)

# Configure structured JSON logging
logging.basicConfig(
    filename="logs/predictions.log",
    level=logging.INFO,
    format="%(message)s"
)

logger = logging.getLogger(__name__)

# Path to the saved Week 4 model
MODEL_PATH = "model/heart_disease_model.pkl"

# Load the trained model once when the API starts
model = joblib.load(MODEL_PATH)

MODEL_NAME = "Random Forest"
MODEL_VERSION = "1.0"


@app.route("/health", methods=["GET"])
def health_check():
    """Check whether the API and model are ready."""

    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None,
        "model": MODEL_NAME,
        "model_version": MODEL_VERSION
    })


@app.route("/predict", methods=["POST"])
def predict():
    """Make a heart disease prediction from patient data."""

    try:
        # Get JSON data from the request
        data = request.get_json(silent=True)

        # Check that JSON was provided
        if data is None:
            return jsonify({
                "error": "Request body must contain JSON data."
            }), 400

        # Required features from the Week 4 model
        required_features = [
            "Age",
            "Sex",
            "ChestPainType",
            "RestingBP",
            "Cholesterol",
            "FastingBS",
            "RestingECG",
            "MaxHR",
            "ExerciseAngina",
            "Oldpeak",
            "ST_Slope"
        ]

        # Check for missing features
        missing_features = [
            feature for feature in required_features
            if feature not in data
        ]

        if missing_features:
            return jsonify({
                "error": "Missing required features.",
                "missing_features": missing_features
            }), 400

        # Validate numeric fields
        numeric_fields = [
            "Age",
            "RestingBP",
            "Cholesterol",
            "FastingBS",
            "MaxHR",
            "Oldpeak"
        ]

        for field in numeric_fields:
            if not isinstance(data[field], (int, float)):
                return jsonify({
                    "error": "Invalid input type.",
                    "field": field,
                    "message": f"{field} must be a number."
                }), 400

        # Validate binary numeric field
        if data["FastingBS"] not in [0, 1]:
            return jsonify({
                "error": "Invalid value.",
                "field": "FastingBS",
                "message": "FastingBS must be either 0 or 1."
            }), 400

        # Validate categorical fields
        allowed_values = {
            "Sex": ["M", "F"],
            "ChestPainType": ["ATA", "NAP", "ASY", "TA"],
            "RestingECG": ["Normal", "ST", "LVH"],
            "ExerciseAngina": ["Y", "N"],
            "ST_Slope": ["Up", "Flat", "Down"]
        }

        for field, valid_values in allowed_values.items():
            if data[field] not in valid_values:
                return jsonify({
                    "error": "Invalid categorical value.",
                    "field": field,
                    "message": (
                        f"{field} must be one of: {valid_values}"
                    )
                }), 400

        # Create a Pandas DataFrame
        # This is required because the Week 4 pipeline
        # selects columns by their column names.
        input_data = pd.DataFrame([{
            "Age": data["Age"],
            "Sex": data["Sex"],
            "ChestPainType": data["ChestPainType"],
            "RestingBP": data["RestingBP"],
            "Cholesterol": data["Cholesterol"],
            "FastingBS": data["FastingBS"],
            "RestingECG": data["RestingECG"],
            "MaxHR": data["MaxHR"],
            "ExerciseAngina": data["ExerciseAngina"],
            "Oldpeak": data["Oldpeak"],
            "ST_Slope": data["ST_Slope"]
        }], columns=required_features)

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Get prediction probabilities
        probabilities = model.predict_proba(input_data)[0]

        # Prepare prediction response
        response_data = {
            "prediction": int(prediction),
            "probability_no_heart_disease": round(
                float(probabilities[0]), 4
            ),
            "probability_heart_disease": round(
                float(probabilities[1]), 4
            ),
            "model": MODEL_NAME,
            "model_version": MODEL_VERSION
        }

        # Log request, output, and timestamp
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": data,
            "output": response_data,
            "status": "success"
        }

        logger.info(json.dumps(log_data))

        return jsonify(response_data)

    except Exception as e:

        # Log failed prediction request
        error_log = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": data if "data" in locals() else None,
            "output": {
                "error": str(e)
            },
            "status": "error"
        }

        logger.error(json.dumps(error_log))

        return jsonify({
            "error": "Prediction failed.",
            "details": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)