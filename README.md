# SMART HEALTHCARE CONSULTANT

## Overview

Smart Healthcare Consultant is a modern healthcare illness detection system with an AI-powered healthcare web application that predicts possible illnesses based on user symptoms using Machine Learning and Large Language Models (LLMs).

The system allows users to:

* Select symptoms from a modern web interface
* Predict possible illnesses using a trained ML model
* Receive AI-generated healthcare guidance
* View disease descriptions, precautions, and treatment suggestions

---

# Features

* Modern healthcare dashboard UI
* Symptom-based illness prediction
* Machine Learning integration
* LLM-based medical explanation retrieval
* Real-time predictions
* Responsive web design
* Flask backend integration
* Professional healthcare interface

---

# Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* Random Forest Classifier
* Pandas
* NumPy

## AI / LLM Integration

* Google Gemini API
* Gemini 2.0 Flash Model

---

# Machine Learning Workflow

1. Dataset is loaded using Pandas
2. Features and labels are separated
3. Data is split into training and testing sets
4. Random Forest Classifier is trained
5. Model accuracy is evaluated
6. Trained model is saved using Pickle
7. Flask application loads the trained model
8. User symptoms are passed for prediction
9. Gemini LLM generates healthcare explanations

---

# Project Structure

```bash
illness-detection/
│
├── data/
│   └── illness_dataset.csv
│
├── model/
│   └── model.pkl
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── static/
│   ├── style.css
│   └── images/
│
├── templates/
│   ├── home.html
│   └── predict.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Running the Project

## Train Model

```bash
python src/train.py
```

---

## Start Flask Application

```bash
python app.py
```

---

# Gemini API Setup

1. Visit Google AI Studio
2. Create API Key
3. Copy API Key
4. Paste API Key inside `app.py`
   
---

# How It Works

1. User selects symptoms
2. Flask receives symptom data
3. ML model predicts illness
4. Gemini LLM generates medical explanation
5. Results are displayed on the same webpage

---

# Example Prediction Flow

```text
Symptoms Selected
        ↓
Machine Learning Prediction
        ↓
Predicted Illness
        ↓
Gemini AI Explanation
        ↓
Healthcare Guidance Displayed
```

---

# Future Improvements

* Doctor appointment booking
* Voice-based symptom input
* Multi-language support
* User authentication system
* Medical history tracking
* Cloud deployment
* Database integration
* Chatbot assistant

---

# Screenshots

## Home Page

* Modern healthcare landing page
* Responsive UI
* Navigation bar
* Symptom checker section

## Prediction Page

* Symptom selection
* Illness prediction
* AI-generated healthcare guidance

