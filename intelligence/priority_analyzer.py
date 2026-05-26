# =========================================================
# Heimdal Operational Priority Analyzer
#
# Purpose:
# Analyze telemetry executions and determine
# operational priority levels.
#
# Responsibilities:
# - Calculate operational priority scores
# - Classify telemetry urgency
# - Support escalation awareness
# - Prioritize operator attention
#
# Philosophy:
# Detection without understanding creates noise.
# Detection with interpretation creates intelligence.
# =========================================================

def calculate_priority_score(execution):
    """
    Calculate operational priority score.
    """
    # Track operational priority score
    score = 0

    # Elevate priority for high operational risk
    if execution.risk == "HIGH RISK":
        score += 5

    # Elevate priority for degraded stability
    if execution.stability == "DEGRADED":
        score += 3
    
    # Increase priority based on finding density
    score += len(execution.findings)

    return score

# =========================================================
# Priority Classification Logic
#
# Convert numerical operational scores into
# explainable priority classifications.
# =========================================================
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