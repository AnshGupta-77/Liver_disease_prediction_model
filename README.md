# Liver Disease Prediction System

A machine learning web application for predicting liver disease based on patient medical data. Built with FastAPI backend, Next.js frontend, and scikit-learn ML models.

## 📌 Project Overview

The Liver Disease Prediction System is a full-stack machine learning application designed to predict whether a patient is likely to suffer from liver disease based on medical attributes. The project features a clean architecture with separate backend and frontend, proper model persistence, and a professional user interface.

## 🎯 Features

- **ML Pipeline**: Support Vector Machine (SVM) classifier with probability-based confidence scores
- **Data Preprocessing**: Automated feature scaling and label encoding
- **REST API**: FastAPI backend with health check and prediction endpoints
- **Modern UI**: Clean, responsive Next.js frontend with Tailwind CSS
- **Model Persistence**: Trained models saved using joblib for easy loading
- **Error Handling**: Comprehensive error handling and validation

## 🛠 Tech Stack

### Backend
- **Python 3.12**
- **FastAPI** - Modern web framework for building APIs
- **scikit-learn** - Machine learning library
- **pandas & numpy** - Data manipulation
- **joblib** - Model serialization
- **uvicorn** - ASGI server

### Frontend
- **Next.js 14** - React framework
- **Tailwind CSS** - Utility-first CSS framework
- **React Hooks** - State management

### ML Models
- **Support Vector Machine (SVM)** - Primary classification model with RBF kernel
- **Naive Bayes** - Alternative model option

## 📊 Dataset

The system uses the Indian Liver Patient Dataset with the following features:
- Age
- Gender
- Total Bilirubin
- Direct Bilirubin
- Alkaline Phosphotase
- Alamine Aminotransferase
- Aspartate Aminotransferase
- Total Proteins
- Albumin
- Albumin and Globulin Ratio

**Target**: Dataset (1 = Liver Disease, 2 = No Liver Disease)

## 🏗 Project Structure

```
Liver_disease_prediction_model/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   ├── routes/
│   │   │   └── prediction.py   # API endpoints
│   │   ├── ml/
│   │   │   ├── model.py        # Model training and prediction
│   │   │   └── preprocessing.py # Data preprocessing
│   │   ├── schemas/
│   │   │   └── prediction.py   # Pydantic schemas
│   │   └── utils/
│   ├── train_model.py          # Model training script
│   └── main.py                 # Server entry point
├── frontend/
│   ├── pages/
│   │   ├── index.js            # Main prediction page
│   │   ├── _app.js             # App component
│   │   └── _document.js        # Document component
│   ├── styles/
│   │   └── globals.css         # Global styles
│   ├── package.json
│   ├── tailwind.config.js
│   └── next.config.js
├── dataset/
│   └── liver.csv               # Training dataset
├── models/                     # Saved models (created after training)
├── notebooks/                  # Jupyter notebooks for analysis
├── requirements.txt            # Python dependencies
└── README.md
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.12 or higher
- Node.js 18 or higher
- npm or yarn

### Backend Setup

1. Navigate to the project directory:
```bash
cd Liver_disease_prediction_model
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Train the model:
```bash
cd backend
python train_model.py
```

5. Start the backend server:
```bash
python main.py
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 📡 API Endpoints

### Health Check
```
GET /api/health
```
Returns API status and model loading information.

### Prediction
```
POST /api/predict
```
Predicts liver disease based on patient features.

**Request Body:**
```json
{
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
```

**Response:**
```json
{
  "prediction": 1,
  "confidence": 0.85,
  "message": "Patient is likely to have liver disease"
}
```

### API Documentation
Interactive API documentation available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧠 ML Workflow

1. **Data Loading**: Load dataset from CSV file
2. **Preprocessing**:
   - Handle missing values (drop rows with NaN)
   - Label encode gender (Male/Female → 0/1)
   - Standard scale all features
3. **Model Training**: Train SVM classifier with RBF kernel
4. **Model Evaluation**: Calculate accuracy on test set
5. **Model Persistence**: Save model and preprocessor using joblib
6. **Prediction**: Load model, preprocess input, predict with confidence

## 📈 Model Performance

The SVM model achieves approximately 70-75% accuracy on the test set. The model includes probability estimation to provide confidence scores for predictions.

## 🔧 Configuration

### Backend Configuration
- Server host: `0.0.0.0` (configurable in `backend/main.py`)
- Server port: `8000` (configurable in `backend/main.py`)
- Model path: `backend/models/liver_disease_svm.joblib`

### Frontend Configuration
- Development server: `localhost:3000`
- API endpoint: `http://localhost:8000/api/predict` (configurable in `frontend/pages/index.js`)

## � Usage

1. Ensure the backend server is running and model is trained
2. Open the frontend application in your browser
3. Fill in the patient medical data form
4. Click "Predict Liver Disease"
5. View the prediction result with confidence score

## ⚠️ Important Notes

- This is a demonstration project for educational purposes
- Predictions should not be used for actual medical diagnosis
- Always consult healthcare professionals for medical advice
- The model is trained on a limited dataset and may not generalize well

## 🚀 Deployment

### Backend Deployment
1. Deploy backend to a cloud platform (Render, Railway, AWS, etc.)
2. Set environment variables for production
3. Ensure model file is included in deployment
4. Configure CORS for production frontend domain

### Frontend Deployment
1. Build the frontend: `npm run build`
2. Deploy to Vercel, Netlify, or similar platform
3. Update API endpoint to production backend URL

## 🔮 Future Enhancements

- [ ] Add hyperparameter tuning for better model performance
- [ ] Implement model versioning
- [ ] Add more ML algorithms (Random Forest, XGBoost)
- [ ] Include feature importance visualization
- [ ] Add user authentication
- [ ] Implement prediction history
- [ ] Add data export functionality
- [ ] Integrate with real medical databases

## 📚 Key Learnings

- End-to-end ML project development
- FastAPI for building production-ready APIs
- Next.js for modern web applications
- Model serialization and deployment
- Data preprocessing and feature engineering
- API design and documentation
- Frontend-backend integration

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

Developed as a machine learning portfolio project.

---

**Note**: This project is intended for educational and demonstration purposes only. It should not be used for actual medical diagnosis or treatment decisions.
