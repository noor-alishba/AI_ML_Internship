# ❤️ Heart Failure Prediction using Machine Learning

A complete Machine Learning project that predicts whether a patient has heart disease using the **Heart Failure Prediction Dataset** and **Logistic Regression**. The project follows an end-to-end Machine Learning workflow, from data exploration to model evaluation, using Scikit-learn Pipeline.

---

## 📌 Project Overview

This project aims to predict the presence of heart disease based on a patient's medical information. It includes data preprocessing, visualization, model training, evaluation, and bonus features such as Cross-Validation and Hyperparameter Tuning.

---

## 🎯 Objectives

- 📂 Load and explore the dataset
- 🧹 Preprocess the data
- 📊 Visualize important patterns
- 🤖 Train a Machine Learning model
- 📈 Evaluate model performance
- ⭐ Implement bonus features

---

## 📁 Dataset Information

- **Dataset:** Heart Failure Prediction Dataset
- **Total Records:** 918
- **Problem Type:** Binary Classification
- **Target Variable:** `HeartDisease`

---

## ⚙️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 🎨 Seaborn
- 🤖 Scikit-learn
- 📓 Jupyter Notebook

---

## 🚀 Project Workflow

### 📥 Data Loading
- Imported required libraries
- Loaded the dataset
- Displayed dataset information

### 🔍 Exploratory Data Analysis (EDA)
- Checked dataset shape
- Viewed data types
- Examined missing values
- Generated statistical summary

### 📊 Data Visualization
- Age Distribution
- Heart Disease Distribution
- Chest Pain Type Distribution
- Correlation Heatmap
- ROC Curve
- Confusion Matrix
- Other exploratory charts

### 🛠 Data Preprocessing
- Selected features and target
- Identified categorical columns
- Applied One-Hot Encoding
- Used ColumnTransformer
- Split data into training and testing sets

### 🤖 Model Building
- Created a Scikit-learn Pipeline
- Trained a Logistic Regression model
- Generated predictions

### 📈 Model Evaluation
- Accuracy Score
- Confusion Matrix
- Classification Report
- Actual vs Predicted Comparison
- ROC Curve

---

## ⭐ Bonus Features

- ✅ 5-Fold Cross Validation
- ✅ GridSearchCV Hyperparameter Tuning
- ✅ Logistic Regression Coefficient Interpretation
- ✅ Class Distribution Analysis
- ✅ Scikit-learn Pipeline

---

## 📂 Project Structure

```text
Heart_Failure_Prediction/
│
├── data/
│   └── heart.csv
│
├── notebooks/
│   └── Heart_Failure_Prediction.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

1. Clone the repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Open the Jupyter Notebook.
4. Run all cells from top to bottom.

---

## 📌 Results

The Logistic Regression model was evaluated using:

- ✅ Accuracy Score
- ✅ Confusion Matrix
- ✅ Classification Report
- ✅ ROC Curve
- ✅ Cross Validation

The model successfully predicts whether a patient is likely to have heart disease based on the provided medical attributes.

---

## 💡 Future Improvements

- Try additional Machine Learning models.
- Perform advanced feature engineering.
- Build a web application using Flask or Streamlit.
- Deploy the trained model online.

---

## 👩‍💻 Author

**Noor Alishba Sajid**

BS Artificial Intelligence  
University of Engineering and Technology (UET), Lahore

---