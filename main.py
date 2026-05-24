from queries.telemetry_queries import (
    get_high_risk_executions,
    get_degraded_executions,
    get_executions_by_endpoint,
    get_executions_by_finding
)

from ingestion.index_reader import load_execution_index

from intelligence.posture_analyzer import (
    analyze_operational_posture
)

from intelligence.severity_analyzer import (
    analyze_severity_distribution
)

from intelligence.finding_analyzer import (
    analyze_finding_totals
)

from intelligence.endpoint_analyzer import (
    analyze_endpoint_activity
)

from intelligence.priority_analyzer import (
    calculate_priority_score,
    classify_priority
)

INDEX_PATH = "execution_index.json"

execution_history = load_execution_index(INDEX_PATH)

# =========================
# Operational Posture
# =========================

operational_posture = analyze_operational_posture(
    execution_history
)

print("\n=== OPERATIONAL POSTURE ===\n")

print(
    operational_posture["posture"]
)

print("\nReasons:")

for reason in operational_posture["reasons"]:
    print(f"- {reason}")

# =========================
# Severity Distribution
# =========================

severity_distribution = (
    analyze_severity_distribution(
        execution_history
    )
)

print("\n=== SEVERITY DISTRIBUTION ===\n")

for severity, count in severity_distribution.items():
    print(f"{severity}: {count}")

total_findings = analyze_finding_totals(
    execution_history
)

print("\n=== FINDING TOTALS ===\n")

print(f"Total Findings: {total_findings}")

endpoint_activity = analyze_endpoint_activity(
    execution_history
)

# =========================
# Endpoint Activity
# =========================

print("\n=== ENDPOINT ACTIVITY ===\n")

for endpoint, count in endpoint_activity.items():
    print(f"{endpoint}: {count}")

# =========================
# Priority Analysis
# =========================

print("\n=== PRIORITY ANALYSIS ===\n")

for execution in execution_history:

    priority_score = (
        calculate_priority_score(
            execution
        )
    )

    priority_label = classify_priority(
        priority_score
    )

    print(
        f"{execution.endpoint} | "
        f"Priority: {priority_label} | "
        f"Score: {priority_score}"
    )

# =========================
# High Risk Executions
# =========================

high_risk_executions = get_high_risk_executions(
    execution_history
)

print("\n=== HIGH RISK EXECUTIONS ===\n")

for execution in high_risk_executions:
    print(execution.summary())

# =========================
# Degraded Executions
# =========================

degraded_executions = get_degraded_executions(
    execution_history
)

print("\n=== DEGRADED EXECUTIONS ===\n")

for execution in degraded_executions:
    print(execution.summary())

# =========================
# Endpoint Executions
# =========================

endpoint_executions = get_executions_by_endpoint(
    execution_history,
    "GET /invalid-endpoint"
)

print("\n=== ENDPOINT EXECUTIONS ===\n")

for execution in endpoint_executions:
    print(execution.summary())

# =========================
# Finding Executions
# =========================

finding_executions = get_executions_by_finding(
    execution_history,
    "Missing Security Headers"
)

print("\n=== FINDING EXECUTIONS ===\n")

for execution in finding_executions:
    print(execution.summary())