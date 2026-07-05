
from preservation_utils import safe_extract

# =========================================================
# Heimdal Severity Distribution Analyzer
#
# Purpose:
# Analyze telemetry severity distribution across
# operational findings.
#
# Responsibilities:
# - Measure LOW severity findings
# - Measure MEDIUM severity findings
# - Measure HIGH severity findings
# - Analyze operational pressure concentration
#
# Philosophy:
# Detection without understanding creates noise.
# Detection with interpretation creates intelligence.
# =========================================================

def analyze_severity_distribution(executions):
    """
    Analyze finding severity distribution across telemetry.
    """

    severity_counts = {
        "LOW": 0,
        "MEDIUM": 0,
        "HIGH": 0
    }

    for execution in executions: 

        findings = safe_extract(
            execution, 
            "findings",
            []
        )
        
        # Analyze telemetry execution findings
        for finding in findings:

            severity = finding.get(
                "severity",
                ""
            ).upper()


            # Track operational severity distribution
            if severity in severity_counts:
                severity_counts[severity] += 1

    return severity_counts