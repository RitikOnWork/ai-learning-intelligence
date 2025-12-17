import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("data/training_data.csv")

X = data[["time_spent", "score"]]
y = data["completed"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "models/completion_model.pkl")

print("Model trained and saved successfully")
