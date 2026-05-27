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

    for execution in executions:

        endpoint_counts[endpoint] = (
            endpoint_counts.get(endpoint, 0) + 1
        )
        recurring_patterns = []
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
