# =========================================================
# Correlation Analyzer Imports
#
# Responsible for operational resilience
# utility imports and analyzer support.
# =========================================================

from preservation_utils import safe_extract

# =========================================================
# Heimdal Historical Pattern Analyzer
#
# Purpose:
# Analyze recurring telemetry behavior
# across operational history to identify
# persistent patterns and trends.
#
# Responsibilities:
# - Detect recurring operational behavior
# - Identify repeated endpoint activity
# - Track recurring risk patterns
# - Support long-term operational awareness
#
# Philosophy:
# Intelligence grows stronger when systems
# remember what repeatedly occurs.
#
# Observe.
# Remember.
# Correlate.
# Learn.
# =========================================================

def analyze_operational_correlation(executions): 
    correlation_detected = False
    correlation_reasons = []

    for execution in executions: 

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

        endpoint_name = safe_extract(
            execution,
            "endpoint",
            "UNKNOWN-ENDPOINT"
            )

        if (
            risk_state == "HIGH RISK"
            and
            stability_state == "DEGRADED"
        ): 
            correlation_detected = True
            correlation_reasons.append(
                f"Correlated HIGH RISK and "
                f"DEGRADED stability detected "
                f"for {endpoint_name}."
            )

    return {
        "correlation_detected": (
            correlation_detected
        ), 
        "reasons": correlation_reasons
    }
   

