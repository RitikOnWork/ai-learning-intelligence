import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "completion_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_completion_ml(time_spent: float, score: float) -> bool:
    features = np.array([[time_spent, score]])
    prediction = model.predict(features)[0]
    return bool(prediction)
