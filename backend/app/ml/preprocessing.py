"""
Data preprocessing utilities for liver disease prediction.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from typing import Tuple


class LiverDataPreprocessor:
    """Handles preprocessing of liver disease dataset."""
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.feature_columns = None
        
    def fit_transform(self, data: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray]:
        """
        Fit preprocessor on data and transform it.
        
        Args:
            data: Raw dataframe with features and target
            
        Returns:
            Tuple of (X_scaled, y) where X is scaled features and y is target
        """
        # Drop missing values
        data_clean = data.dropna()
        
        # Store feature columns (excluding target)
        self.feature_columns = [col for col in data_clean.columns if col != 'Dataset']
        
        # Encode gender
        if 'Gender' in data_clean.columns:
            data_clean['Gender'] = self.label_encoder.fit_transform(data_clean['Gender'])
        
        # Separate features and target
        X = data_clean[self.feature_columns]
        y = data_clean['Dataset']
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled, y.values
    
    def transform(self, data: pd.DataFrame) -> np.ndarray:
        """
        Transform new data using fitted preprocessor.
        
        Args:
            data: Raw dataframe with features
            
        Returns:
            Scaled features as numpy array
        """
        # Encode gender
        if 'Gender' in data.columns:
            data = data.copy()
            data['Gender'] = self.label_encoder.transform(data['Gender'])
        
        # Select features
        X = data[self.feature_columns]
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        return X_scaled
