MediGuard: Intelligent Heart Disease Risk Assessment System

1. Problem Statement

Cardiovascular disease (CVD) remains the leading cause of death globally. Current diagnostic processes often involve expert analysis and specialized, expensive tests (like angiography or advanced ECG), which are not always readily available in primary care settings or resource-limited areas.
The core problem is the lack of an accessible, rapid, and reliable initial screening tool that can use standard physiological metrics (Age, Blood Pressure, Cholesterol, etc.) to give a patient or practitioner a high-probability risk assessment. This delay in initial screening leads to postponed intervention and poorer patient outcomes.
MediGuard addresses this by leveraging Machine Learning to automate this critical first step of risk assessment.

2. Scope of the Project

The primary goal of the MediGuard project is to build a fully functional, self-contained Python application capable of training an AI model and performing real-time risk predictions based on user input.

In Scope:
i) Data Generation: Creation of a synthetic, but logically consistent, medical dataset for training.
ii) Model Implementation: Training and validation of a Random Forest Classifier model. 
![licensed-image](https://github.com/user-attachments/assets/6226b131-dfeb-4de2-adb1-bdc301a4e828)

iii) User Interface: A clean, secure Command Line Interface (CLI) for data input and result display.
iv) Authentication: Basic security checks to restrict access to the system.

Out of Scope:
i) Integration with real-world hospital databases (EHR/EMR systems).
ii) Deployment as a full web or mobile application.
iii) Handling of complex medical imaging data (e.g., X-rays, CT scans).

3. Target Users

The system is designed to be utilized by two primary groups:
A. Target User- General Practitioners (GPs)
  Primary Goal- Quick pre-diagnostic screening in a clinic setting.
  System Use Case- Input basic vitals during a patient consultation to justify the need for specialist referral or further testing.

B. Target User- Health Informatics Students / Researchers
  Primary Goal- Testing and validating different machine learning models.
  System Use Case- Access the system's core logic to swap out classifiers (e.g., try Logistic Regression or SVM) and measure performance.

4. High-Level Features
The system is composed of four main modules:
i) Secure Authentication Module:
Allows login via predefined credentials (doctor/admin123).
Restricts access to the diagnostic features to authorized users only.

ii) Data Management Module:
Automatically generates a 300-record dataset upon first run.
Loads and processes the dataset for immediate model training.

iii) Intelligent Risk Assessment Engine (AIML Module):
Trains a Random Forest Classifier to learn patterns from age, BP, and cholesterol.
Accepts new patient parameters as input.
Outputs a definitive prediction: "High Risk ⚠️" or "Low Risk ✅".

iv) Reporting & Feedback Module:
Displays the AI model's training accuracy (e.g., 88.5%).
Presents the final risk diagnosis clearly and concisely to the user.
