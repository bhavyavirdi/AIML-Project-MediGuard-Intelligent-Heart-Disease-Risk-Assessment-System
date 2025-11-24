import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import sys
import time

class DataManager:
    """Handles the creation of synthetic medical data for training."""
   
    def get_data(self, n_samples=300):
        """Generates synthetic heart data for demonstration purposes."""
        np.random.seed(42)
       
               data = {
            'age': np.random.randint(30, 80, n_samples),
            'bp': np.random.randint(90, 180, n_samples),      # Systolic Blood Pressure
            'chol': np.random.randint(150, 500, n_samples),   # Cholesterol levels
            'sugar': np.random.randint(0, 2, n_samples),      # 1 = Diabetic, 0 = Non-Diabetic
            'risk': []
        }

                for i in range(n_samples):
            # Normalizing values roughly to create a risk score
            risk_score = (data['age'][i]/80) + (data['bp'][i]/180) + (data['chol'][i]/500)
           
                       data['risk'].append(1 if risk_score > 1.8 else 0)
           
        return pd.DataFrame(data)

class RiskModel:
    """The Machine Learning engine using Random Forest."""
   
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.accuracy = 0.0

    def train(self, df):
        """Splits data and trains the model."""
        print(" [System] Training AI Model...", end=" ")
       
        X = df.drop('risk', axis=1) # Features
        y = df['risk']              # Target
       
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
       
        self.model.fit(X_train, y_train)
       
                preds = self.model.predict(X_test)
        self.accuracy = accuracy_score(y_test, preds)
       
        time.sleep(1) # Simulating processing time for user experience
        print(f"Done! (Accuracy: {self.accuracy*100:.1f}%)")

    def predict(self, age, bp, chol, sugar):
        """Takes patient vitals and returns a prediction."""
        # Input must be a 2D array: [[age, bp, chol, sugar]]
        result = self.model.predict([[age, bp, chol, sugar]])
        return "HIGH RISK ⚠️" if result[0] == 1 else "Low Risk ✅"

def login_screen():
    """Simple authentication system."""
    print("\n" + "="*30)
    print("   🏥 MediGuard Secure Login   ")
    print("="*30)
   
    attempts = 3
    while attempts > 0:
        user
