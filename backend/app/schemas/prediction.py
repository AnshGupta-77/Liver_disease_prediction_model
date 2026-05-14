"""
Pydantic schemas for request/response validation.
"""
from pydantic import BaseModel, Field
from typing import Optional


class PatientFeatures(BaseModel):
    """Schema for patient input features."""
    
    age: int = Field(..., ge=0, le=120, description="Patient age in years")
    gender: str = Field(..., description="Patient gender (Male/Female)")
    total_bilirubin: float = Field(..., ge=0, description="Total Bilirubin level")
    direct_bilirubin: float = Field(..., ge=0, description="Direct Bilirubin level")
    alkaline_phosphotase: int = Field(..., ge=0, description="Alkaline Phosphotase level")
    alamine_aminotransferase: int = Field(..., ge=0, description="Alamine Aminotransferase level")
    aspartate_aminotransferase: int = Field(..., ge=0, description="Aspartate Aminotransferase level")
    total_protiens: float = Field(..., ge=0, description="Total Proteins level")
    albumin: float = Field(..., ge=0, description="Albumin level")
    albumin_and_globulin_ratio: float = Field(..., ge=0, description="Albumin and Globulin Ratio")
    
    class Config:
        json_schema_extra = {
            "example": {
                "age": 65,
                "gender": "Female",
                "total_bilirubin": 0.7,
                "direct_bilirubin": 0.1,
                "alkaline_phosphotase": 187,
                "alamine_aminotransferase": 16,
                "aspartate_aminotransferase": 18,
                "total_protiens": 6.8,
                "albumin": 3.3,
                "albumin_and_globulin_ratio": 0.9
            }
        }


class PredictionResponse(BaseModel):
    """Schema for prediction response."""
    
    prediction: int = Field(..., description="Prediction result (1 = Liver Disease, 2 = No Liver Disease)")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score (0-1)")
    message: str = Field(..., description="Human-readable prediction message")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prediction": 1,
                "confidence": 0.85,
                "message": "Patient is likely to have liver disease"
            }
        }


class HealthResponse(BaseModel):
    """Schema for health check response."""
    
    status: str = Field(..., description="API status")
    model_loaded: bool = Field(..., description="Whether the ML model is loaded")
    model_type: Optional[str] = Field(None, description="Type of loaded model")
