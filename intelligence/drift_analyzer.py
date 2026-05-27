# =========================================================
# Heimdal Operational Drift Analyzer
#
# Purpose:
# Detect deviations between current telemetry
# behavior and established operational
# baselines.
#
# Responsibilities:
# - Compare current telemetry against baseline
# - Detect operational drift patterns
# - Identify abnormal behavioral deviations
# - Support anomaly awareness evolution
#
# Philosophy:
# Intelligence emerges when systems recognize
# deviation from expected behavior.
#
# Observe.
# Compare.
# Detect.
# Adapt.
# =========================================================

def analyze_operational_drift(
    executions,
    baseline
):
    drift_detected = False
    drift_reason = []
    for execution in executions:
        if execution.risk != baseline["common_risk"]:
            drift_detected = True
            drift_reason.append(
                f"Risk drift detected: "
                f"{execution.risk} differs from "
                f"baseline {baseline['common_risk']}."
            )
    return{
        "drift_detected":  drift_detected,
        "reasons": drift_reason
            }