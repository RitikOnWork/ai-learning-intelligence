import joblib
import numpy as np

# Load model once (important for performance)
model = joblib.load("models/completion_model.pkl")

def predict_completion_ml(time_spent: float, score: float) -> bool:
    """
    Predict course completion using trained ML model
    """
    features = np.array([[time_spent, score]])
    prediction = model.predict(features)[0]
    return bool(prediction)