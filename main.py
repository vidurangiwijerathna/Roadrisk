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
async def predict_risk(data: dict):
    try:
        # Convert categorical values to numbers
        lighting_map = {"daylight": 0, "dim": 1, "night": 2}
        weather_map = {"clear": 0, "rainy": 1, "foggy": 2}
        road_type_map = {"rural": 0, "urban": 1, "highway": 2}
        time_map = {"morning": 0, "afternoon": 1, "evening": 2}

        df = pd.DataFrame([[
            int(data["public_road"]),
            int(data["road_signs_present"]),
            lighting_map[data["lighting"]],
            weather_map[data["weather"]],
            road_type_map[data["road_type"]],
            time_map[data["time_of_day"]],
            int(data["holiday"]),
            int(data["school_season"]),
            int(data["num_reported_accidents"]),
            int(data["num_lanes"]),
            float(data["curvature"]),
            float(data["speed_limit"])
        ]], columns=feature_names)

        # Get probability instead of class
        prediction = float(best_model.predict(df)[0])


        # Risk classification
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
        return {"error": str(e)}


# -----------------------------
# Root
# -----------------------------
@app.get("/")
def home():
    return {"message": "Road Accident Risk Prediction API is running 🚦"}
