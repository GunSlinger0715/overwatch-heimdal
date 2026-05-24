def analyze_finding_totals(executions):
    """
    Count total findings across telemetry.
    """

    total_findings = 0

    for execution in executions:
        total_findings += len(
            execution.findings
        )

    return total_findings