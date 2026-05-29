# =========================================================
# Historical Pattern Analyzer Imports
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
def analyze_historical_patterns(executions): 

    endpoint_counts = {}
    recurring_patterns = []

    for execution in executions:

        endpoint = safe_extract(
            execution, 
            "endpoint",
            "UNKNOWN-ENDPOINT"
        )

        endpoint_counts[endpoint] = (
            endpoint_counts.get(endpoint, 0) + 1
        )

    for endpoint, count in endpoint_counts.items():
        if count >= 2: 
            recurring_patterns.append(
                f"Endpoint {endpoint} appeared "
                f"{count} times historically."
            )
    return {
        "patterns_detected": (
            len(recurring_patterns) > 0
        ), 
        "patterns": recurring_patterns
    }
