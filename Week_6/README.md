# ❤️ Heart Disease Prediction ML API

A machine learning API that predicts the likelihood of heart disease using a trained **Random Forest Classifier**. The project includes a Flask-based ML API, FastAPI deployment adapter, API-key authentication, input validation, batch prediction, structured logging, and an interactive HTML frontend.

## 🚀 Live Deployment

🌐 **Live API:**  
YOUR_FASTAPI_CLOUD_URL

❤️ **Health Check:**  
YOUR_FASTAPI_CLOUD_URL/health

🔮 **Prediction Endpoint:**  
YOUR_FASTAPI_CLOUD_URL/predict

## 🤖 Model Description

The project uses a **Random Forest** machine learning classifier for heart disease prediction.

The model uses the following patient features:

- 👤 Age
- ⚥ Sex
- ❤️ Chest Pain Type
- 🩸 Resting Blood Pressure
- 🧪 Cholesterol
- 🍬 Fasting Blood Sugar
- 📈 Resting ECG
- 💓 Maximum Heart Rate
- 🏃 Exercise Angina
- 📊 Oldpeak
- 📉 ST Slope

## 📥 Input Format

The `/predict` endpoint accepts patient information in JSON format:

```json
{
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
```
## 📤 Output Format

The API returns the prediction and probability scores:

{
    "prediction": 0,
    "probability_no_heart_disease": 0.85,
    "probability_heart_disease": 0.15,
    "model": "Random Forest",
    "model_version": "1.0"
}
0 = No heart disease detected by the model
1 = Heart disease detected by the model

## 🔐 Authentication

The /predict and /predict/batch endpoints require an API key.

The API key must be provided through the following HTTP header:

X-API-Key: YOUR_API_KEY

🔒 The API key is stored using an environment variable and is not hard-coded in the source code.

🛣️ API Endpoints
❤️ GET /health

Checks whether the API and trained model are available.

🔮 POST /predict

Generates a prediction for a single patient.

## 📦 POST /predict/batch

Generates predictions for multiple patient records.

## 🏠 GET /

Opens the interactive heart disease prediction interface.

## ✨ Features
🤖 Random Forest heart disease prediction
🌐 Public cloud deployment
❤️ Health monitoring endpoint
🔮 Single patient prediction
📦 Batch prediction
🔐 API-key authentication
✅ Input validation
📝 Structured prediction logging
🖥️ Interactive HTML frontend
🔒 Environment-based secret configuration

## 📁 Project Structure
Week_6/
│
├── app.py
├── fastapi_app.py
├── pyproject.toml
├── requirements.txt
│
├── model/
│   └── heart_disease_model.pkl
│
├── templates/
│   └── index.html
│
└── README.md

## ⚙️ Local Setup

Clone the repository and navigate to the Week 6 directory:

cd Week_6

Install the required dependencies:

pip install -r requirements.txt

Run the Flask application:

python app.py

The local application will be available at:

http://127.0.0.1:5000
## ☁️ Deployment

The API is deployed publicly using FastAPI Cloud.

The existing Flask ML application is served through a FastAPI deployment adapter.

Sensitive configuration such as the API key is provided through environment variables.

## ⚠️ Known Limitations
The model's predictions depend on the quality and representativeness of the training dataset.
The model should not be considered a medical diagnostic system.
Predictions should not replace professional medical advice.
The model is static and does not automatically retrain with new data.
Performance may vary for patients whose characteristics differ from the training data.
The prediction API requires a valid API key.
🔮 Future Improvements
📊 Improve model performance through hyperparameter tuning and cross-validation.
🧠 Add model explainability using techniques such as SHAP.
📈 Add production monitoring and uptime checks.
🔄 Add CI/CD for automated deployment.
🔐 Improve authentication and rate limiting.
🧪 Expand automated API and model testing.