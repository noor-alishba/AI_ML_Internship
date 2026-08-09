import sys
import os
import pytest

# Add the Week_5 project directory to Python's import path
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def valid_patient_data():
    """Return valid sample patient data."""
    return {
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


def test_health_endpoint(client):
    """Test that the health endpoint is working."""
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["model_loaded"] is True


def test_prediction_success(client):
    """Test a valid prediction request."""
    response = client.post(
        "/predict",
        json=valid_patient_data()
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
    assert "probability_no_heart_disease" in data
    assert "probability_heart_disease" in data
    assert "model" in data
    assert "model_version" in data


def test_prediction_missing_feature(client):
    """Test prediction with a missing required feature."""
    data = valid_patient_data()

    del data["Age"]

    response = client.post(
        "/predict",
        json=data
    )

    assert response.status_code == 400

    result = response.get_json()

    assert "missing_features" in result
    assert "Age" in result["missing_features"]


def test_prediction_without_json(client):
    """Test prediction when no JSON data is provided."""
    response = client.post("/predict")

    assert response.status_code == 400

    result = response.get_json()

    assert "error" in result


def test_prediction_invalid_data_type(client):
    """Test prediction with an invalid data type."""
    data = valid_patient_data()

    data["Age"] = "fifty-two"

    response = client.post(
        "/predict",
        json=data
    )

    assert response.status_code == 400

    result = response.get_json()

    assert result["error"] == "Invalid input type."
    assert result["field"] == "Age"


def test_prediction_invalid_categorical_value(client):
    """Test prediction with an invalid categorical value."""
    data = valid_patient_data()

    data["Sex"] = "X"

    response = client.post(
        "/predict",
        json=data
    )

    assert response.status_code == 400

    result = response.get_json()

    assert result["error"] == "Invalid categorical value."
    assert result["field"] == "Sex"


def test_prediction_response_values(client):
    """Test that prediction values have valid ranges."""
    response = client.post(
        "/predict",
        json=valid_patient_data()
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["prediction"] in [0, 1]

    assert 0 <= data["probability_no_heart_disease"] <= 1
    assert 0 <= data["probability_heart_disease"] <= 1