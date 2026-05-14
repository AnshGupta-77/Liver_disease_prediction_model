"""
Model training and management for liver disease prediction.
"""
import numpy as np
import pandas as pd
import joblib
from pathlib import Path
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from typing import Dict, Tuple, Optional
import os

from .preprocessing import LiverDataPreprocessor


class LiverDiseaseModel:
    """Manages training, saving, and loading of liver disease prediction models."""
    
    def __init__(self, model_dir: str = "models"):
        self.model_dir = Path(model_dir)
        self.model_dir.mkdir(exist_ok=True)
        
        self.preprocessor = LiverDataPreprocessor()
        self.model = None
        self.model_name = None
        
    def load_data(self, data_path: str) -> pd.DataFrame:
        """Load dataset from CSV file."""
        return pd.read_csv(data_path)
    
    def train(self, data_path: str, model_type: str = "svm") -> Dict[str, float]:
        """
        Train a model on the liver disease dataset.
        
        Args:
            data_path: Path to the CSV dataset
            model_type: Type of model to train ('svm' or 'nb')
            
        Returns:
            Dictionary with training metrics
        """
        # Load data
        data = self.load_data(data_path)
        
        # Preprocess
        X, y = self.preprocessor.fit_transform(data)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Initialize model
        if model_type == "svm":
            self.model = SVC(C=1, tol=0.0001, gamma='scale', kernel='rbf', probability=True)
            self.model_name = "svm"
        elif model_type == "nb":
            self.model = GaussianNB()
            self.model_name = "nb"
        else:
            raise ValueError(f"Unsupported model type: {model_type}")
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        metrics = {
            "accuracy": accuracy,
            "model_type": model_type
        }
        
        return metrics
    
    def predict(self, features: Dict) -> Tuple[int, float]:
        """
        Make prediction on new patient data.
        
        Args:
            features: Dictionary of patient features
            
        Returns:
            Tuple of (prediction, confidence_score)
        """
        if self.model is None:
            raise ValueError("Model not loaded. Call load_model() first.")
        
        # Convert to DataFrame
        feature_df = pd.DataFrame([features])
        
        # Preprocess
        X_scaled = self.preprocessor.transform(feature_df)
        
        # Predict
        prediction = self.model.predict(X_scaled)[0]
        
        # Get confidence score
        if hasattr(self.model, 'predict_proba'):
            probabilities = self.model.predict_proba(X_scaled)[0]
            confidence = max(probabilities)
        else:
            confidence = 0.0
        
        return int(prediction), float(confidence)
    
    def save_model(self, filename: Optional[str] = None) -> str:
        """
        Save trained model and preprocessor.
        
        Args:
            filename: Optional custom filename
            
        Returns:
            Path to saved model
        """
        if self.model is None:
            raise ValueError("No model to save. Train a model first.")
        
        if filename is None:
            filename = f"liver_disease_{self.model_name}.joblib"
        
        model_path = self.model_dir / filename
        
        # Save model and preprocessor together
        joblib.dump({
            'model': self.model,
            'preprocessor': self.preprocessor,
            'model_name': self.model_name
        }, model_path)
        
        return str(model_path)
    
    def load_model(self, model_path: str) -> None:
        """
        Load trained model and preprocessor.
        
        Args:
            model_path: Path to saved model file
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        # Load model and preprocessor
        artifacts = joblib.load(model_path)
        self.model = artifacts['model']
        self.preprocessor = artifacts['preprocessor']
        self.model_name = artifacts['model_name']
