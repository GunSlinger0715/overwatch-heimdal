def calculate_priority_score(execution):
    """
    Calculate operational priority score.
    """

    score = 0

    if execution.risk == "HIGH RISK":
        score += 5

    if execution.stability == "DEGRADED":
        score += 3

    score += len(execution.findings)

    return score

def classify_priority(score):
    """
    Classify operational priority.
    """

    if score >= 12:
        return "CRITICAL"

    if score >= 8:
        return "HIGH"

    if score >= 4:
        return "MEDIUM"

    return "LOW"