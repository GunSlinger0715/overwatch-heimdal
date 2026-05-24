def analyze_operational_posture(executions):
    """
    Analyze operational posture based on execution telemetry.
    """

    high_risk_count = 0
    degraded_count = 0

    posture_reasons = []

    for execution in executions:

        if execution.risk == "HIGH RISK":
            high_risk_count += 1

        if execution.stability == "DEGRADED":
            degraded_count += 1

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