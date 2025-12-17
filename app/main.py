from fastapi import FastAPI
from app.schemas import StudentInput
from pipeline.risk_logic import calculate_risk
from pipeline.insights import detect_chapter_difficulty, generate_insight
from pipeline.ml_inference import predict_completion_ml

app = FastAPI(title="AI Learning Intelligence Tool")

@app.get("/")
def home():
    return {"message": "AI Learning Intelligence Tool is running"}

@app.post("/analyze")
def analyze_student(data: StudentInput):
    risk_level = calculate_risk(data.time_spent, data.score)
    will_complete = predict_completion_ml(data.time_spent, data.score)
    chapter_info = detect_chapter_difficulty(data.time_spent, data.score)
    insight = generate_insight(
        risk_level,
        will_complete,
        chapter_info["difficulty_level"]
    )

    return {
        "student_id": data.student_id,
        "course_id": data.course_id,
        "chapter_order": data.chapter_order,
        "time_spent": data.time_spent,
        "score": data.score,
        "risk_level": risk_level,
        "will_complete_course": will_complete,
        "chapter_difficulty": chapter_info,
        "insight": insight
    }
