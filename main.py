# =========================================================
# Heimdal Operational Intelligence Pipeline
#
# Purpose:
# Execute operational telemetry analysis and derive
# explainable intelligence conclusions from GateKeeper
# execution telemetry.
#
# Responsibilities:
# - Load telemetry execution history
# - Analyze operational posture
# - Measure severity distribution
# - Analyze finding density
# - Analyze endpoint activity
# - Prioritize operational telemetry
# - Determine escalation conditions
# - Display operational evidence
#
# Philosophy:
# Detection without understanding creates noise.
# Detection with interpretation creates intelligence.
# =========================================================


# =========================================================
# Query Layer Imports
#
# Responsible for telemetry filtering, correlation,
# and operational investigation queries.
# =========================================================

from queries.telemetry_queries import (
    get_high_risk_executions,
    get_degraded_executions,
    get_executions_by_endpoint,
    get_executions_by_finding
)

# =========================================================
# Ingestion Layer Imports
#
# Responsible for loading and normalizing telemetry
# execution history from storage.
# =========================================================

from ingestion.index_reader import load_execution_index

# =========================================================
# Intelligence Layer Imports
#
# Responsible for operational interpretation,
# reasoning, prioritization, and escalation analysis.
# =========================================================

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

from intelligence.escalation_analyzer import (
    analyze_escalation
)

# =========================================================
# Telemetry Source Configuration
# =========================================================

INDEX_PATH = "execution_index.json"

# =========================================================
# Load Execution History
#
# Load normalized telemetry execution history for
# operational analysis and interpretation.
# =========================================================

execution_history = load_execution_index(INDEX_PATH)

# =========================================================
# Operational Posture Analysis
#
# Analyze overall operational telemetry posture based
# on risk levels and stability conditions.
#
# Goal:
# Transform raw telemetry into explainable operational
# awareness.
# =========================================================

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

# =========================================================
# Severity Distribution Analysis
#
# Measure telemetry pressure distribution across
# LOW, MEDIUM, and HIGH severity findings.
#
# Goal:
# Understand operational severity concentration.
# =========================================================

severity_distribution = (
    analyze_severity_distribution(
        execution_history
    )
)

print("\n=== SEVERITY DISTRIBUTION ===\n")

for severity, count in severity_distribution.items():
    print(f"{severity}: {count}")

# =========================================================
# Finding Density Analysis
#
# Measure total operational issue volume across
# telemetry execution history.
#
# Goal:
# Understand operational issue density and pressure.
# =========================================================

total_findings = analyze_finding_totals(
    execution_history
)

print("\n=== FINDING TOTALS ===\n")

print(f"Total Findings: {total_findings}")

# =========================================================
# Endpoint Activity Analysis
#
# Analyze recurring operational activity by endpoint.
#
# Goal:
# Identify operational hotspots and recurring
# telemetry concentration areas.
# =========================================================

endpoint_activity = analyze_endpoint_activity(
    execution_history
)

# =========================
# Endpoint Activity
# =========================

print("\n=== ENDPOINT ACTIVITY ===\n")

for endpoint, count in endpoint_activity.items():
    print(f"{endpoint}: {count}")

# =========================================================
# Operational Priority Analysis
#
# Prioritize telemetry executions based on:
# - Risk level
# - Stability degradation
# - Finding density
#
# Goal:
# Identify telemetry requiring immediate
# operator attention.
# =========================================================

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

# =========================================================
# Escalation Awareness Analysis
#
# Determine whether operational conditions require
# elevated operator awareness or escalation.
#
# Goal:
# Identify critical operational conditions requiring
# immediate attention.
# =========================================================

escalation_status = analyze_escalation(
    execution_history
)

print("\n=== ESCALATION STATUS ===\n")

print(
    f"Escalation Required: "
    f"{escalation_status['escalation']}"
)

print(
    f"Reason: "
    f"{escalation_status['reason']}"
)