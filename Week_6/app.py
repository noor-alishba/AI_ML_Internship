from flask import Flask, jsonify, request, render_template
import joblib
import pandas as pd
import logging
import os
import json
import secrets
from datetime import datetime, timezone
from functools import wraps
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# LOGGING

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/predictions.log",
    level=logging.INFO,
    format="%(message)s"
)

logger = logging.getLogger(__name__)


# MODEL CONFIGURATION

MODEL_PATH = "model/heart_disease_model.pkl"

# Load the trained model once when the API starts
model = joblib.load(MODEL_PATH)

MODEL_NAME = "Random Forest"
MODEL_VERSION = "1.0"


# API KEY CONFIGURATION

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    API_KEY = secrets.token_urlsafe(32)

    print(
        "WARNING: API_KEY not found in .env. "
        "A temporary API key was generated."
    )

    print("Temporary API Key:", API_KEY)


def require_api_key(func):
    """Protect an endpoint using an API key."""

    @wraps(func)
    def decorated(*args, **kwargs):

        provided_key = request.headers.get("X-API-Key")

        if not provided_key or not secrets.compare_digest(
            provided_key,
            API_KEY
        ):
            return jsonify({
                "error": "Unauthorized.",
                "message": "A valid X-API-Key header is required."
            }), 401

        return func(*args, **kwargs)

    return decorated


# MODEL FEATURES

REQUIRED_FEATURES = [
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


NUMERIC_FIELDS = [
    "Age",
    "RestingBP",
    "Cholesterol",
    "FastingBS",
    "MaxHR",
    "Oldpeak"
]


ALLOWED_VALUES = {
    "Sex": ["M", "F"],
    "ChestPainType": ["ATA", "NAP", "ASY", "TA"],
    "RestingECG": ["Normal", "ST", "LVH"],
    "ExerciseAngina": ["Y", "N"],
    "ST_Slope": ["Up", "Flat", "Down"]
}


# VALIDATION

def validate_patient_data(data):
    """Validate one patient record."""

    if not isinstance(data, dict):
        return {
            "error": "Invalid input.",
            "message": "Patient data must be a JSON object."
        }

    # Check required features
    missing_features = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in data
    ]

    if missing_features:
        return {
            "error": "Missing required features.",
            "missing_features": missing_features
        }

    # Validate numeric fields
    for field in NUMERIC_FIELDS:

        if isinstance(data[field], bool) or not isinstance(
            data[field],
            (int, float)
        ):
            return {
                "error": "Invalid input type.",
                "field": field,
                "message": f"{field} must be a number."
            }

    # Validate FastingBS
    if data["FastingBS"] not in [0, 1]:
        return {
            "error": "Invalid value.",
            "field": "FastingBS",
            "message": "FastingBS must be either 0 or 1."
        }

    # Validate categorical fields
    for field, valid_values in ALLOWED_VALUES.items():

        if data[field] not in valid_values:
            return {
                "error": "Invalid categorical value.",
                "field": field,
                "message": (
                    f"{field} must be one of: {valid_values}"
                )
            }

    return None


# PREDICTION FUNCTION

def make_prediction(data):
    """Generate a prediction for one patient."""

    input_data = pd.DataFrame(
        [{
            feature: data[feature]
            for feature in REQUIRED_FEATURES
        }],
        columns=REQUIRED_FEATURES
    )

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    return {
        "prediction": int(prediction),
        "probability_no_heart_disease": round(
            float(probabilities[0]),
            4
        ),
        "probability_heart_disease": round(
            float(probabilities[1]),
            4
        ),
        "model": MODEL_NAME,
        "model_version": MODEL_VERSION
    }


# HOME

@app.route("/", methods=["GET"])
def home():
    """Serve the HTML frontend."""

    return render_template("index.html")


# HEALTH CHECK

@app.route("/health", methods=["GET"])
def health_check():
    """Check whether the API and model are ready."""

    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None,
        "model": MODEL_NAME,
        "model_version": MODEL_VERSION
    })


# SINGLE PREDICTION API

@app.route("/predict", methods=["POST"])
@require_api_key
def predict():
    """Make a prediction for one patient using the protected API."""

    data = request.get_json(silent=True)

    # Check JSON
    if data is None:
        return jsonify({
            "error": "Request body must contain JSON data."
        }), 400

    # Validate input
    validation_error = validate_patient_data(data)

    if validation_error:
        return jsonify(validation_error), 400

    try:

        response_data = make_prediction(data)

        # Structured logging
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input": data,
            "output": response_data,
            "status": "success",
            "source": "api"
        }

        logger.info(json.dumps(log_data))

        return jsonify(response_data)

    except Exception as e:

        error_log = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input": data,
            "output": {
                "error": str(e)
            },
            "status": "error",
            "source": "api"
        }

        logger.error(json.dumps(error_log))

        return jsonify({
            "error": "Prediction failed.",
            "details": str(e)
        }), 500


# FRONTEND PREDICTION

@app.route("/predict-ui", methods=["POST"])
def predict_ui():
    """
    Handle predictions submitted through the HTML frontend.

    This endpoint is intentionally separate from /predict
    because the browser frontend does not expose the API key.
    """

    data = request.get_json(silent=True)

    # Check JSON
    if data is None:
        return jsonify({
            "error": "Request body must contain JSON data."
        }), 400

    # Validate input
    validation_error = validate_patient_data(data)

    if validation_error:
        return jsonify(validation_error), 400

    try:

        response_data = make_prediction(data)

        # Structured logging
        logger.info(json.dumps({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input": data,
            "output": response_data,
            "status": "success",
            "source": "frontend"
        }))

        return jsonify(response_data)

    except Exception as e:

        logger.error(json.dumps({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "input": data,
            "output": {
                "error": str(e)
            },
            "status": "error",
            "source": "frontend"
        }))

        return jsonify({
            "error": "Prediction failed.",
            "details": str(e)
        }), 500


# BATCH PREDICTION

@app.route("/predict/batch", methods=["POST"])
@require_api_key
def predict_batch():
    """Make predictions for multiple patient records."""

    data = request.get_json(silent=True)

    # Check JSON
    if data is None:
        return jsonify({
            "error": "Request body must contain JSON data."
        }), 400

    

    if not isinstance(data, dict) or "records" not in data:
        return jsonify({
            "error": "Request must contain a 'records' list."
        }), 400

    records = data["records"]

    if not isinstance(records, list):
        return jsonify({
            "error": "'records' must be a list."
        }), 400

    if len(records) == 0:
        return jsonify({
            "error": "'records' cannot be empty."
        }), 400

    results = []

    # Process each patient
    for index, record in enumerate(records):

        validation_error = validate_patient_data(record)

        if validation_error:
            return jsonify({
                "error": "Invalid record.",
                "record_index": index,
                "details": validation_error
            }), 400

        try:

            prediction = make_prediction(record)

            results.append({
                "record_index": index,
                **prediction
            })

        except Exception as e:

            return jsonify({
                "error": "Batch prediction failed.",
                "record_index": index,
                "details": str(e)
            }), 500

    # Final response
    response_data = {
        "count": len(results),
        "results": results,
        "model": MODEL_NAME,
        "model_version": MODEL_VERSION
    }

    # Structured logging
    logger.info(json.dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input": data,
        "output": response_data,
        "status": "success",
        "source": "batch_api"
    }))

    return jsonify(response_data)


# RUN APPLICATION

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )