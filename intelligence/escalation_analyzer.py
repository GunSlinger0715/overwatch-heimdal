# =========================================================
# Escalation Analyzer Imports
#
# Responsible for operational resilience
# utility imports and analyzer support.
# =========================================================
from preservation_utils import safe_extract

# =========================================================
# Heimdal Escalation Awareness Analyzer
#
# Purpose:
# Determine whether operational telemetry conditions
# require elevated awareness or escalation.
#
# Responsibilities:
# - Detect critical operational conditions
# - Evaluate telemetry severity concentration
# - Trigger escalation awareness
# - Support operator decision-making
#
# Philosophy:
# Detection without understanding creates noise.
# Detection with interpretation creates intelligence.
# =========================================================
def analyze_escalation(executions):
    """
    Determine if operational escalation is necessary.
    """

    # Track critical operational conditions
    critical_count = 0

    # Analyze telemetry execution history
    for execution in executions:

    # Safely extract operational telemetry indicators

        risk = safe_extract(
            execution,
            "risk",
            "UNKNOWN"
        )

        findings = safe_extract(
            execution,
            "findings",
            []
        )

        findings_count = len(findings)

        # Detect escalation-worthy operational conditions
        if (
            risk == "HIGH RISK"
            and findings_count >= 5
            ):
                critical_count += 1

    # Trigger operational escalation awareness
    if critical_count >= 1:
        return {
            "escalation": True,
            "reason": "Critical operational conditions detected"
        }

    return {
        "escalation": False,
        "reason": "No escalation required"
    }