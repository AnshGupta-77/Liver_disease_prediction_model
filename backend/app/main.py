"""
Main FastAPI application for liver disease prediction API.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.prediction import router as prediction_router

# Create FastAPI app
app = FastAPI(
    title="Liver Disease Prediction API",
    description="Machine Learning API for predicting liver disease based on patient medical data",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(prediction_router, prefix="/api", tags=["prediction"])


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Liver Disease Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/health",
            "predict": "/api/predict",
            "docs": "/docs"
        }
    }
