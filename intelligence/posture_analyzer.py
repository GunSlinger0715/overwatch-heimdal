# =========================================================
# Heimdal Operational Posture Analyzer
#
# Purpose:
# Analyze telemetry execution history and derive
# overall operational posture awareness.
#
# Responsibilities:
# - Detect elevated operational risk
# - Analyze stability degradation
# - Generate explainable reasoning
# - Provide operational posture summaries
#
# Philosophy:
# Detection without understanding creates noise.
# Detection with interpretation creates intelligence.
# =========================================================
def analyze_operational_posture(executions):
    """
    Analyze operational posture based on execution telemetry.
    """

    high_risk_count = 0
    degraded_count = 0

    # Store explainable operational reasoning

    posture_reasons = []

    # Analyze telemetry execution history

    for execution in executions:
        
        # Detect elevated operational risk
        if execution.risk == "HIGH RISK":
            high_risk_count += 1
        # Detect degraded operational stability
        if execution.stability == "DEGRADED":
            degraded_count += 1

    # Track elevated operational risk conditions
    if high_risk_count >= 1:
        posture_reasons.append(
            "HIGH RISK executions detected"
        )

    if degraded_count >= 1:
        posture_reasons.append(
            "DEGRADED stability detected"
        )

    if high_risk_count >= 1 and degraded_count >= 1:
        posture = "ELEVATED RISK"

    elif high_risk_count >= 1:
        posture = "HIGH RISK POSTURE"

    elif degraded_count >= 1:
        posture = "DEGRADED POSTURE"

    else:
        posture = "STABLE"

    return {
        "posture": posture,
        "reasons": posture_reasons
    }