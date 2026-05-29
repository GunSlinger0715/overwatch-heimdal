# =========================================================
# Finding Analyzer Imports
#
# Responsible for operational resilience
# utility imports and analyzer support.
# =========================================================
from preservation_utils import safe_extract

# =========================================================
# Heimdal Finding Density Analyzer
#
# Purpose:
# Analyze operational finding density across
# telemetry execution history.
#
# Responsibilities:
# - Measure total finding volume
# - Analyze operational issue density
# - Detect elevated telemetry pressure
#
# Philosophy:
# Detection without understanding creates noise.
# Detection with interpretation creates intelligence.
# =========================================================
def analyze_finding_totals(executions):
    """
    Count total findings across telemetry.
    """
    # Track total operational finding volume
    total_findings = 0
    
    # Analyze telemetry execution findings

    for execution in executions: 

        findings = safe_extract(
            execution, 
            "findings",
            []
        )

        total_findings += len(
            findings
        )
        
    # Measure finding density contribution
    return total_findings