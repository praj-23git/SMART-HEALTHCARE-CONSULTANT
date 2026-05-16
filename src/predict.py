import pickle
import numpy as np

# Load trained model
with open("../model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Example symptom input for the dataset columns:
# Fever, Cough, Headache, Nausea, Vomiting, Diarrhea, Rash,
# ShortnessBreath, Fatigue, LossSmellTaste, Sneezing, SoreThroat,
# BlurredVision, ChillsSweating, JointMusclePain, AbdominalPain
sample = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]])

# Predict illness
prediction = model.predict(sample)

print("Predicted Illness:", prediction[0])