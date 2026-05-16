# MODERN HEALTHCARE CONSULTANT

## Overview

Modern Healthcare Consultant is a smart healthcare illness detection system with an AI-powered healthcare web application that predicts possible illnesses based on user symptoms using Machine Learning and Large Language Models (LLMs).

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

*<ins>HOMEPAGE SCREENSHOT</ins>

<img width="938" height="499" alt="Screenshot-frontpage" src="https://github.com/user-attachments/assets/189c3581-1aae-4f06-8c82-f8bf63bae0fa" />

---

*<ins>LEARN MORE SCREENSHOT</ins>

<img width="936" height="500" alt="Screenshot-learn more" src="https://github.com/user-attachments/assets/7bd4bf3f-0c08-4e5b-8a15-e3122c224379" />

---

*<ins>SYMTOPMS CHECK SCREENSHOT</ins>

<img width="938" height="503" alt="screenshot-2" src="https://github.com/user-attachments/assets/343781c4-c12b-45fc-ae25-33496a0ffaf4" />

<img width="855" height="499" alt="screenshot-1" src="https://github.com/user-attachments/assets/739c2033-0bb9-47f2-929f-c67933fa2e3c" />

---

*<ins>ILLNESS PREDICTION SCREENSHOT</ins>

<img width="773" height="397" alt="screenshot-3" src="https://github.com/user-attachments/assets/4744313a-2589-428d-8c70-43aeca04909d" />


## Home Page

* Modern healthcare landing page
* Responsive UI
* Navigation bar
* Symptom checker section

## Prediction Page

* Symptom selection
* Illness prediction
* AI-generated healthcare guidance

