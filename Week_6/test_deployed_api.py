import os
import pytest
import requests
from getpass import getpass

# LIVE API CONFIGURATION

LIVE_API_URL = os.getenv(
    "LIVE_API_URL",
    "https://heart-disease-api-62ff8e29.fastapicloud.dev"
).rstrip("/")


# TEST PATIENT

PATIENT_DATA = {
    "Age": 52,
    "Sex": "M",
    "ChestPainType": "ATA",
    "RestingBP": 130,
    "Cholesterol": 250,
    "FastingBS": 0,
    "RestingECG": "Normal",
    "MaxHR": 150,
    "ExerciseAngina": "N",
    "Oldpeak": 1.0,
    "ST_Slope": "Up"
}


@pytest.fixture(scope="session")
def api_key():
    """
    Get the API key without storing it in the test file.
    """

    key = os.getenv("API_KEY")

    if not key:
        key = getpass("Enter your deployed API key: ")

    return key


@pytest.fixture
def headers(api_key):
    return {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }


# HEALTH TEST

def test_live_health_endpoint():

    response = requests.get(
        f"{LIVE_API_URL}/health",
        timeout=30
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["model_loaded"] is True
    assert data["model"] == "Random Forest"
    assert data["model_version"] == "1.0"


# LIVE PREDICTION TEST

def test_live_prediction(headers):

    response = requests.post(
        f"{LIVE_API_URL}/predict",
        json=PATIENT_DATA,
        headers=headers,
        timeout=30
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "probability_no_heart_disease" in data
    assert "probability_heart_disease" in data
    assert "model" in data
    assert "model_version" in data

    assert data["prediction"] in [0, 1]

    assert 0 <= data["probability_no_heart_disease"] <= 1
    assert 0 <= data["probability_heart_disease"] <= 1

    assert data["model"] == "Random Forest"
    assert data["model_version"] == "1.0"


# UNAUTHORIZED REQUEST TEST

def test_live_prediction_without_api_key():

    response = requests.post(
        f"{LIVE_API_URL}/predict",
        json=PATIENT_DATA,
        timeout=30
    )

    assert response.status_code == 401

    data = response.json()

    assert data["error"] == "Unauthorized."