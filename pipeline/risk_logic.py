def calculate_risk(time_spent: float, score: float) -> str:
    """
    Simple early risk detection logic
    """
    if score < 40 and time_spent < 30:
        return "HIGH"
    elif score < 60:
        return "MEDIUM"
    else:
        return "LOW"
