# LearnSight AI 🚀  
AI-Powered Learning Intelligence Tool

---

## 📌 Overview
**LearnSight AI** is an AI-powered Learning Intelligence Tool designed for internship and training platforms.  
It analyzes learner behavior data to generate intelligent predictions and actionable insights for mentors and administrators.

Unlike notebook-based experiments, LearnSight AI is a **production-style, executable AI system** exposed via a REST API.

This project was developed as part of a **Data Science & Machine Learning Internship Assessment**, focusing on real-world AI deployment, not experimentation.

---

## 🎯 Objectives
The tool aims to:
- Predict whether a student will complete a course
- Detect at-risk students early
- Identify difficult chapters in a course
- Generate human-readable insights for mentors/admins
- Demonstrate end-to-end AI engineering and deployment

---

## ✨ Key Features
- ✅ Course Completion Prediction (ML-based, Binary Classification)
- 🚨 Early Risk Detection (Low / Medium / High)
- 📘 Chapter Difficulty Detection
- 💡 Human-Readable Insight Generation
- ⚙️ REST API Interface (FastAPI)
- ☁️ Live Cloud Deployment (Render)
- 📦 Saved & Loaded ML Model (Joblib)

---

## 🧠 AI Capabilities

### 1. Course Completion Prediction
- **Type:** Binary Classification
- **Model:** Logistic Regression (Scikit-learn)
- **Output:** Will complete / Will not complete

### 2. Early Risk Detection
- Rule-based logic using engagement signals
- Flags learners as **LOW**, **MEDIUM**, or **HIGH** risk

### 3. Chapter Difficulty Detection
- Uses:
  - Time spent
  - Assessment score
- Outputs difficulty level:
  - EASY / MEDIUM / HARD

### 4. Insight Generation
Generates mentor-friendly insights such as:
- Students requiring immediate intervention
- Chapters needing content improvement
- Overall learner progress summary

---

Input Data (JSON)
↓
Preprocessing & Validation
↓
Feature Engineering
↓
ML Model Inference
↓
Risk & Difficulty Analysis
↓
Insight Generation
↓
API Output (JSON)


---

## 🛠️ Technology Stack
- **Language:** Python 3.10
- **Backend Framework:** FastAPI
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Model Persistence:** Joblib
- **Deployment:** Render (Cloud)
- **API Docs:** Swagger UI

---

## 📁 Project Structure
```
ai-learning-intelligence/
│
├── app/
│ ├── main.py
│ ├── schemas.py
│
├── pipeline/
│ ├── risk_logic.py
│ ├── completion_logic.py
│ ├── insights.py
│ ├── ml_inference.py
│
├── training/
│ └── train_model.py
│
├── models/
│ └── completion_model.pkl
│
├── data/
│ └── training_data.csv
│
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RitikOnWork/ai-learning-intelligence.git
cd ai-learning-intelligence

```
```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Access the Tool
API: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs

🌐 Live Deployment

Deployed API URL:
* URL: [Learnsight AI](https://learnsight-ai.onrender.com)

Swagger UI:
* URL: [Learnsight AI](https://learnsight-ai.onrender.com/docs)

### 📥 Sample Input
```bash
{
  "student_id": "S101",
  "course_id": "C-AI-01",
  "chapter_order": 3,
  "time_spent": 50,
  "score": 70
}
```
### 📤 Sample Output
```bash
{
  "student_id": "S101",
  "course_id": "C-AI-01",
  "chapter_order": 3,
  "time_spent": 50,
  "score": 70,
  "risk_level": "LOW",
  "will_complete_course": true,
  "chapter_difficulty": {
    "difficulty_score": 0.4,
    "difficulty_level": "MEDIUM"
  },
  "insight": "Student is progressing well with no immediate risks."
}
```

## 🧑‍💻 Author

**Ritik Raj**
AI/ML Enthusiast | Python Developer | Problem Solver

* GitHub: [RitikOnWork](https://github.com/RitikOnWork)

---

### ⭐ If you find this repository helpful, consider giving it a star!

