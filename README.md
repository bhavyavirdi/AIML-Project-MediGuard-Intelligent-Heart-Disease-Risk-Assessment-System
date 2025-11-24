# AIML-Project-MediGuard-Intelligent-Heart-Disease-Risk-Assessment-System
MediGuard: Intelligent Heart Disease Risk Assessment System A modular Python-based Machine Learning application designed to predict cardiovascular risk. It utilizes a Random Forest Classifier to analyze patient vitals (Age, BP, Cholesterol) and provides real-time health assessments with a secure, user-friendly CLI.
# 🏥 MediGuard: Intelligent Heart Disease Risk Assessment System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![ML](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green) ![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Project Overview
**MediGuard** is an AI-powered diagnostic tool designed to assist in the early detection of heart disease. Cardiovascular diseases are a leading cause of global mortality, often due to delayed diagnosis. MediGuard solves this by offering a quick, accessible, and data-driven risk assessment using Machine Learning.

This project implements a **Layered Architecture** to ensure modularity, separating data handling, authentication, and the AI prediction engine.

## 🚀 Key Features
* **🔐 Secure Authentication:** Role-based login system (Doctor/Admin) to protect system access.
* **🧠 Intelligent Prediction:** Uses a **Random Forest Classifier** to analyze complex non-linear relationships between health parameters.
* **📊 Synthetic Data Engine:** Includes a built-in module to generate realistic medical datasets for training and testing purposes.
* **📉 Risk Analytics:** detailed analysis of patient vitals (Age, Blood Pressure, Cholesterol, Blood Sugar).
* **✅ Real-time Diagnosis:** Instant classification of patients into "High Risk" or "Low Risk" categories.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** * `pandas` (Data Manipulation)
    * `numpy` (Numerical computations)
    * `scikit-learn` (Machine Learning implementation)
* **Interface:** Command Line Interface (CLI) for robustness and speed.

## 📂 Project Structure
The project follows a modular design pattern:
Installation & Usage

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/yourusername/MediGuard.git](https://github.com/yourusername/MediGuard.git)
   cd MediGuard
Install Dependencies

Bash

pip install pandas numpy scikit-learn
Run the Application

Bash

python main.py
Login Credentials

Username: doctor

Password: admin123

🧪 How It Works
Initialization: On startup, the system checks for existing data. If none is found, the DataManager generates a synthetic dataset of 300+ patient records.

Training: The RiskModel trains itself on this data to understand the correlation between BP, Cholesterol, Age, and Heart Disease.

Interaction: The user logs in and inputs specific patient details.

Inference: The model calculates the probability and outputs a risk warning (High/Low).

🔮 Future Enhancements
Integration with a Web Interface (Flask/Streamlit).

Support for real-world datasets (e.g., UCI Heart Disease Dataset).

Visual graphs for patient history trends.
