# =========================================================
# Heimdal Operational Health Analyzer
#
# Purpose:
# Evaluate overall operational health
# conditions across telemetry intelligence.
#
# Responsibilities:
# - Assess operational environment health
# - Identify unhealthy operational conditions
# - Support resilience awareness
# - Provide high-level operational summaries
#
# Philosophy:
# Healthy systems remain resilient under stress.
#
#
# Operational health analysis must
# degrade gracefully during partial
# analyzer instability or telemetry
# uncertainty.
#
# Observe.
# Evaluate.
# Endure.
# Protect.
# =========================================================

def analyze_operational_health(
        posture_analysis, 
        confidence_analysis, 
        stability_analysis, 
): 
    health = "HEALTHY"
    health_reasons = []

    posture_analysis = posture_analysis or {}
    confidence_analysis = confidence_analysis or {}
    stability_analysis = stability_analysis or {}

    if posture_analysis.get("posture") == "ELEVATED RISK": 
        health = "UNHEALTHY"

        health_reasons.append(
            "Operational posture indicates "
            "elevated environmental risk."
        )

    if confidence_analysis.get("confidence") == "LOW CONFIDENCE":
        health_reasons.append(
            "Low operational confidence "
            "reduces assessment reliability."
        )

    if stability_analysis.get("stability") == "UNSTABLE":
        health_reasons.append(
            "Operational instability detected "
            "across telemetry conditions."
        )

    return {
        "health": health, 
        "reasons": health_reasons
    }