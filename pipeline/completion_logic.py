def predict_completion(time_spent: float, score: float) -> bool:
    """
    Predict whether a student will complete the course
    """
    if time_spent >= 40 and score >= 60:
        return True
    else:
        return False
