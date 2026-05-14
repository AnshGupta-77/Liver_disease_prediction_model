"""
API routes for liver disease prediction.
"""
from fastapi import APIRouter, HTTPException
from typing import Dict
import os

from ..schemas.prediction import PatientFeatures, PredictionResponse, HealthResponse
from ..ml.model import LiverDiseaseModel

router = APIRouter()

# Global model instance
model: LiverDiseaseModel = None
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "..", "models", "liver_disease_svm.joblib")


def get_model() -> LiverDiseaseModel:
    """Get or initialize the model instance."""
    global model
    if model is None:
        model = LiverDiseaseModel()
        # Try to load model if it exists
        if os.path.exists(MODEL_PATH):
            model.load_model(MODEL_PATH)
    return model


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify API status.
    """
    current_model = get_model()
    return HealthResponse(
        status="healthy",
        model_loaded=current_model.model is not None,
        model_type=current_model.model_name if current_model.model else None
    )


@router.post("/predict", response_model=PredictionResponse)
async def predict_liver_disease(features: PatientFeatures) -> PredictionResponse:
    """
    Predict liver disease based on patient features.
    
    Args:
        features: Patient medical features
        
    Returns:
        Prediction result with confidence score
    """
    current_model = get_model()
    
    if current_model.model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please train and save the model first."
        )
    
    try:
        # Convert features to dictionary format expected by model
        feature_dict = {
            'Age': features.age,
            'Gender': features.gender,
            'Total_Bilirubin': features.total_bilirubin,
            'Direct_Bilirubin': features.direct_bilirubin,
            'Alkaline_Phosphotase': features.alkaline_phosphotase,
            'Alamine_Aminotransferase': features.alamine_aminotransferase,
            'Aspartate_Aminotransferase': features.aspartate_aminotransferase,
            'Total_Protiens': features.total_protiens,
            'Albumin': features.albumin,
            'Albumin_and_Globulin_Ratio': features.albumin_and_globulin_ratio
        }
        
        # Make prediction
        prediction, confidence = current_model.predict(feature_dict)
        
        # Generate message
        if prediction == 1:
            message = "Patient is likely to have liver disease"
        else:
            message = "Patient is unlikely to have liver disease"
        
        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,
            message=message
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )
