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

        for finding in execution.findings:

            severity = finding.get(
                "severity",
                ""
            ).upper()

            if severity in severity_counts:
                severity_counts[severity] += 1

    return severity_counts