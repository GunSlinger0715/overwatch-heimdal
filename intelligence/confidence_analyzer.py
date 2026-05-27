# =========================================================
# Heimdal Confidence Analyzer
#
# Purpose:
# Evaluate operational confidence levels associated
# with telemetry interpretation and operational
# conclusions.
#
# Responsibilities:
# - Measure telemetry interpretation confidence
# - Identify ambiguous operational conditions
# - Detect unstable reasoning conditions
# - Support explainable operational certainty
#
# Philosophy:
# Intelligence without confidence awareness
# creates dangerous assumptions.
#
# Observe.
# Interpret.
# Reflect.
# Evaluate.
# =========================================================

def analyze_operational_confidence(executions):
    """
    Analyze operational confidence based on telemetry.
    """

    confidence_score = 0
    confidence_reasons = []

    for execution in executions:
        # Evaluate confidence based on risk and stability
        if execution.risk == "HIGH RISK":
            confidence_score -= 2
            confidence_reasons.append(
                "HIGH RISK telemetry reduces "
                "operational certainty."
            )
        if execution.stability == "DEGRADED":
            confidence_score -= 1
            confidence_reasons.append(
                "DEGRADED stability introduces "
                "operational ambiguity."
        )
        
        # Increase confidence for low-risk, stable conditions
        if execution.risk == "LOW RISK" and execution.stability == "STABLE":
            confidence_score += 2

    # Classify confidence level
    if confidence_score >= 3:
        return {
            "confidence": "HIGH CONFIDENCE",
            "reason":(
                "Multiple operational indicators "
                "strongly agree."
            ), 
            "details": confidence_reasons
}
    elif confidence_score >= 0:
        return {
            "confidence": "MODERATE CONFIDENCE",
            "reason":(
                "Operational indicators partially agree "
                "but ambiguity remains."
            ), 
            "details": confidence_reasons
        }
    else:
        return {
            "confidence": "LOW CONFIDENCE",
            "reason":(
                "Telemetry signals are weak, inconsistent,  "
                "or insufficient for strong conclusions."
            ), 
            "details": confidence_reasons
        }