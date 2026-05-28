# =========================================================
# Heimdal Stability Analyzer
#
# Purpose:
# Evaluate overall operational stability
# conditions across telemetry activity.
#
# Responsibilities:
# - Assess environmental operational stability
# - Detect unstable execution behavior
# - Identify recurring degraded conditions
# - Support operational resilience awareness
#
# Philosophy:
# Stability reveals the true condition
# of operational environments.
#
# Observe.
# Evaluate.
# Stabilize.
# Endure.
# =========================================================

def analyze_operational_stability(executions): 
    
    stable_count = 0
    degraded_count = 0
    stability_reasons = []
    
    stability = "UNKNOWN"

    if not executions: 
        stability_reasons.append(
            "No telemetry executions available for stability evaluation."
        )

    for execution in executions: 
        if execution.stability == "STABLE": 
            stable_count += 1
        
        if execution.stability == "DEGRADED":
            degraded_count += 1
            stability_reasons.append(
                "DEGRADED operational telemetry detected."
            )

    if degraded_count > stable_count: 
        stability = "UNSTABLE"

        stability_reasons.append(
            "Degraded operational conditions exceed stable telemetry activity"
        )
    elif stable_count >= degraded_count: 
        stability = "STABLE"  
    
    return {
        "stability": stability, 
        "stable_executions": stable_count, 
        "degraded_executions": degraded_count, 
        "reasons": stability_reasons
    }