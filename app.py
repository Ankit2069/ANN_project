from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np
import pickle
from tensorflow.keras.models import load_model

app = FastAPI(
    title="ANN Prediction API",
    description="Artificial Neural Network API for customer churn predictions",
    version="1.0.0"
)

# Load model & scaler
print("Loading model and scaler...")
model = load_model("model.h5")
scaler = pickle.load(open("scaler.pkl", "rb"))
print("✓ Model and scaler loaded successfully!")

class PredictionInput(BaseModel):
    """
    Input data for prediction.
    
    Expected input: 10 numeric features
    [CreditScore, Geography(encoded), Gender(encoded), Age, Tenure, Balance, 
     NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]
    
    Example:
    - Geography: France=0, Germany=1, Spain=2
    - Gender: Female=0, Male=1
    """
    data: list = Field(..., description="List of 10 numeric features")

@app.get("/")
def home():
    return {
        "message": "ANN Customer Churn Prediction API is running",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "predict": "POST /predict",
            "health": "GET /health"
        }
    }

@app.post("/predict")
def predict(input: PredictionInput):
    """
    Make a churn prediction using the trained ANN model.
    
    Input: List of 10 features (must be encoded numerically)
    - CreditScore (300-850)
    - Geography (0=France, 1=Germany, 2=Spain)
    - Gender (0=Female, 1=Male)
    - Age (18-96)
    - Tenure (0-10)
    - Balance (0-250000)
    - NumOfProducts (1-4)
    - HasCrCard (0 or 1)
    - IsActiveMember (0 or 1)
    - EstimatedSalary (10000-200000)
    
    Returns:
    - prediction: probability of churn (0-1)
    - confidence: how confident the model is in this prediction
    """
    try:
        if len(input.data) != 10:
            return {"error": f"Expected 10 features, got {len(input.data)}"}
        
        input_data = np.array(input.data).reshape(1, -1)
        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data, verbose=0)
        
        pred_value = float(prediction[0][0])
        
        return {
            "prediction": round(pred_value, 4),
            "churn_probability": round(pred_value * 100, 2),
            "confidence": round(max(pred_value, 1 - pred_value) * 100, 2),
            "status": "High Risk" if pred_value > 0.75 else ("Medium Risk" if pred_value > 0.5 else "Low Risk")
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "ANN Prediction API"}

