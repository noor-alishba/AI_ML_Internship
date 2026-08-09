# Heart Disease Prediction API

## 📌 Project Overview

This project deploys the best-performing heart disease prediction model developed in Week 4 as a Flask REST API.

The API accepts patient health information in JSON format and returns a heart disease prediction along with prediction probabilities.

---

## 🎯 Objectives

- Deploy the trained Week 4 Random Forest model.
- Provide a REST API for heart disease prediction.
- Validate incoming patient data.
- Return prediction probabilities.
- Provide an API health-check endpoint.
- Log prediction requests and responses.
- Implement automated API testing using pytest.

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Pytest
- JSON
- REST API
- Git
- GitHub

---

## 📁 Project Structure

```text
Week_5/
│
├── app.py
├── README.md
├── requirements.txt
│
├── model/
│   └── heart_disease_model.pkl
│
├── logs/
│   └── predictions.log
│
└── tests/
    └── test_api.py