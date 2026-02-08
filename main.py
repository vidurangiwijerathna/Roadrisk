from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load trained Road Risk model
# -----------------------------
best_model = joblib.load("best_model.joblib")

# Feature order must be EXACTLY same as training
feature_names = [
    "public_road",
    "road_signs_present",
    "lighting",
    "weather",
    "road_type",
    "time_of_day",
    "holiday",
    "school_season",
    "num_reported_accidents",
    "num_lanes",
    "curvature",
    "speed_limit"
]

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(title="Road Accident Risk Prediction API")

# -----------------------------
# Input Schema
# -----------------------------
class RoadInput(BaseModel):
    public_road: int
    road_signs_present: int
    lighting: int
    weather: int
    road_type: int
    time_of_day: int
    holiday: int
    school_season: int
    num_reported_accidents: int
    num_lanes: int
    curvature: float
    speed_limit: float

# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
async def predict_risk(data: RoadInput):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([[
            data.public_road,
            data.road_signs_present,
            data.lighting,
            data.weather,
            data.road_type,
            data.time_of_day,
            data.holiday,
            data.school_season,
            data.num_reported_accidents,
            data.num_lanes,
            data.curvature,
            data.speed_limit
        ]], columns=feature_names)

        # Make prediction
        prediction = best_model.predict(df)[0]

        # Convert prediction into risk level
        if prediction < 0.3:
            risk = "Low"
        elif prediction < 0.6:
            risk = "Medium"
        else:
            risk = "High"

        return {
            "accident_risk_score": float(prediction),
            "risk_level": risk
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# Root
# -----------------------------
@app.get("/")
def home():
    return {"message": "Road Accident Risk Prediction API is running 🚦"}
