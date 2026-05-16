import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
data = pd.read_csv("../data/Illness_Dataset.csv")

# Features and target
X = data.drop("Illness", axis=1)
y = data["Illness"]

# Build a stronger model with balanced class support
model = RandomForestClassifier(
    n_estimators=250,
    max_depth=12,
    min_samples_leaf=2,
    class_weight="balanced",
    random_state=42,
)

print("Training the model on the full dataset...")
model.fit(X, y)

# Evaluate training performance on the full dataset
train_accuracy = accuracy_score(y, model.predict(X))
print("Training accuracy:", round(train_accuracy, 3))

# Save model
with open("../model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")