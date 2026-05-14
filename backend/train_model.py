"""
Script to train and save the liver disease prediction model.
Run this script before starting the API server.
"""
import sys
import os
from pathlib import Path

# Add app directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app.ml.model import LiverDiseaseModel


def main():
    """Train and save the model."""
    print("Training Liver Disease Prediction Model...")
    
    # Initialize model
    model = LiverDiseaseModel(model_dir="../models")
    
    # Path to dataset
    data_path = "../dataset/liver.csv"
    
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        return
    
    # Train SVM model (better for this type of classification)
    print("Training SVM model...")
    metrics = model.train(data_path, model_type="svm")
    
    print(f"Training completed!")
    print(f"Model type: {metrics['model_type']}")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    
    # Save model
    model_path = model.save_model()
    print(f"Model saved to: {model_path}")
    
    print("\nModel is ready for predictions!")


if __name__ == "__main__":
    main()
