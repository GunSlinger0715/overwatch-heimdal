# =========================================================
# Endpoint Analyzer Imports
#
# Responsible for operational resilience
# utility imports and analyzer support.
# =========================================================
from preservation_utils import safe_extract

# =========================================================
# Heimdal Endpoint Activity Analyzer
#
# Purpose:
# Analyze recurring endpoint activity across
# telemetry execution history.
#
# Responsibilities:
# - Measure endpoint activity frequency
# - Detect operational hotspots
# - Identify recurring telemetry concentration
# - Support operational correlation analysis
#
# Philosophy:
# Detection without understanding creates noise.
# Detection with interpretation creates intelligence.
# =========================================================
def analyze_endpoint_activity(executions):
    """
    Analyze recurring endpoint activity.
    """
    # Track recurring endpoint activity frequency
    endpoint_counts = {}
    
    # Analyze telemetry execution history
    for execution in executions:
        
        # Safely extract operational endpoint identifier
        endpoint = safe_extract(
            execution,
            "endpoint",
            "UNKNOWN-ENDPOINT"
        )

        # Initialize endpoint activity tracking
        if endpoint not in endpoint_counts:
            endpoint_counts[endpoint] = 0
        
        # Measure recurring endpoint activity
        endpoint_counts[endpoint] += 1

    return endpoint_counts