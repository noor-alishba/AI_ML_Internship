import sys
import os
import pytest

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app import app, API_KEY


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def api_headers():
    """Return valid API authentication headers."""
    return {
        "X-API-Key": API_KEY
    }


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


def test_prediction_success(client, api_headers):
    """Test a valid prediction request."""
    response = client.post(
        "/predict",
        json=valid_patient_data(),
        headers=api_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
    assert "probability_no_heart_disease" in data
    assert "probability_heart_disease" in data
    assert "model" in data
    assert "model_version" in data


def test_prediction_missing_feature(client, api_headers):
    """Test prediction with a missing required feature."""
    data = valid_patient_data()

    del data["Age"]

    response = client.post(
        "/predict",
        json=data,
        headers=api_headers
    )

    assert response.status_code == 400

    result = response.get_json()

    assert "missing_features" in result
    assert "Age" in result["missing_features"]


def test_prediction_without_json(client, api_headers):
    """Test prediction when no JSON data is provided."""
    response = client.post(
        "/predict",
        headers=api_headers
    )

    assert response.status_code == 400

    result = response.get_json()

    assert "error" in result


def test_prediction_invalid_data_type(client, api_headers):
    """Test prediction with an invalid data type."""
    data = valid_patient_data()

    data["Age"] = "fifty-two"

    response = client.post(
        "/predict",
        json=data,
        headers=api_headers
    )

    assert response.status_code == 400

    result = response.get_json()

    assert result["error"] == "Invalid input type."
    assert result["field"] == "Age"


def test_prediction_invalid_categorical_value(client, api_headers):
    """Test prediction with an invalid categorical value."""
    data = valid_patient_data()

    data["Sex"] = "X"

    response = client.post(
        "/predict",
        json=data,
        headers=api_headers
    )

    assert response.status_code == 400

    result = response.get_json()

    assert result["error"] == "Invalid categorical value."
    assert result["field"] == "Sex"


def test_prediction_response_values(client, api_headers):
    """Test that prediction values have valid ranges."""
    response = client.post(
        "/predict",
        json=valid_patient_data(),
        headers=api_headers
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["prediction"] in [0, 1]

    assert 0 <= data["probability_no_heart_disease"] <= 1
    assert 0 <= data["probability_heart_disease"] <= 1


def test_prediction_without_api_key(client):
    """Test that prediction is rejected without an API key."""
    response = client.post(
        "/predict",
        json=valid_patient_data()
    )

    assert response.status_code == 401

    result = response.get_json()

    assert result["error"] == "Unauthorized."


def test_prediction_with_invalid_api_key(client):
    """Test that prediction is rejected with an invalid API key."""
    response = client.post(
        "/predict",
        json=valid_patient_data(),
        headers={
            "X-API-Key": "invalid-key"
        }
    )

    assert response.status_code == 401

    result = response.get_json()

    assert result["error"] == "Unauthorized."


# BATCH PREDICTION TESTS

def test_batch_prediction_success(client, api_headers):
    """Test successful batch prediction."""
    data = {
        "records": [
            valid_patient_data(),
            valid_patient_data()
        ]
    }

    response = client.post(
        "/predict/batch",
        json=data,
        headers=api_headers
    )

    assert response.status_code == 200

    result = response.get_json()

    assert result["count"] == 2
    assert len(result["results"]) == 2
    assert result["model"] == "Random Forest"
    assert result["model_version"] == "1.0"

    assert "prediction" in result["results"][0]
    assert "probability_no_heart_disease" in result["results"][0]
    assert "probability_heart_disease" in result["results"][0]


def test_batch_prediction_empty_records(client, api_headers):
    """Test batch prediction with an empty records list."""
    response = client.post(
        "/predict/batch",
        json={
            "records": []
        },
        headers=api_headers
    )

    assert response.status_code == 400

    result = response.get_json()

    assert result["error"] == "'records' cannot be empty."


def test_batch_prediction_invalid_record(client, api_headers):
    """Test batch prediction with an invalid record."""
    data = valid_patient_data()

    data["Age"] = "fifty-two"

    response = client.post(
        "/predict/batch",
        json={
            "records": [data]
        },
        headers=api_headers
    )

    assert response.status_code == 400

    result = response.get_json()

    assert result["error"] == "Invalid record."
    assert result["record_index"] == 0