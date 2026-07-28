from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI

from src.api.schemas import SalesRequest

# =====================================================
# Create FastAPI App
# =====================================================

app = FastAPI(
    title="SmartMart AI API",
    description="Sales Prediction using Random Forest",
    version="1.0"
)

# =====================================================
# Load Best Model
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "best_model.pkl"

model = joblib.load(MODEL_PATH)

print("✅ Best Model Loaded")

# =====================================================
# Home Route
# =====================================================

@app.get("/")
def home():
    return {
        "message": "Welcome to SmartMart AI Sales Prediction API"
    }

# =====================================================
# Prediction Route
# =====================================================

@app.post("/predict")
def predict(request: SalesRequest):

    data = pd.DataFrame([request.model_dump()])

    print("\nIncoming Data")
    print(data.to_string())

    prediction = model.predict(data)

    print("\nPrediction:", prediction)

    return {
        "predicted_sales": round(float(prediction[0]), 2)
    }