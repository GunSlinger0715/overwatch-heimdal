# =========================================================
# Priority Analyzer Imports
#
# Responsible for operational resilience
# utility imports and analyzer support.
# =========================================================

from preservation_utils import safe_extract

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

        # Safely extract telemetry conditions

    risk_state = safe_extract(
        execution,
        "risk",
        "UNKNOWN"
    )

    stability_state = safe_extract(
        execution,
        "stability",
        "UNKNOWN"
    )

    findings = safe_extract(
        execution,
        "findings",
        []
    )

    # Elevate priority for high operational risk
    if risk_state == "HIGH RISK":
        score += 5

    # Elevate priority for degraded stability
    if stability_state == "DEGRADED":
        score += 3
    
    # Increase priority based on finding density
    score += len(findings)

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