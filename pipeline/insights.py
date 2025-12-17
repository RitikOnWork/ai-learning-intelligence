def detect_chapter_difficulty(time_spent: float, score: float) -> dict:
    """
    Detect chapter difficulty using engagement signals
    """
    difficulty_score = 0

    if time_spent > 50:
        difficulty_score += 0.4
    if score < 50:
        difficulty_score += 0.6

    if difficulty_score >= 0.7:
        level = "HARD"
    elif difficulty_score >= 0.4:
        level = "MEDIUM"
    else:
        level = "EASY"

    return {
        "difficulty_score": round(difficulty_score, 2),
        "difficulty_level": level
    }


def generate_insight(risk_level: str, will_complete: bool, chapter_level: str) -> str:
    """
    Generate human-readable insight
    """
    if risk_level == "HIGH":
        return "Student is at high risk and requires immediate mentor intervention."
    if not will_complete:
        return "Student is likely to drop out without support."
    if chapter_level == "HARD":
        return "Chapter appears difficult and may need content improvement."

    return "Student is progressing well with no immediate risks."
