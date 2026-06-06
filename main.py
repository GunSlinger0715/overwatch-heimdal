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
# Baseline Intelligence Imports
#
# Responsible for operational baseline
# awareness, telemetry pattern tracking,
# and deviation detection foundations.
# =========================================================

from intelligence.baseline_analyzer import (
    analyze_operational_baseline
)
# =========================================================
# Drift Intelligence Imports
#
# Responsible for operational deviation
# detection, behavioral drift analysis,
# and anomaly awareness evolution.
# =========================================================

from intelligence.drift_analyzer import (
    analyze_operational_drift
)

# =========================================================
# Correlation Intelligence Imports
#
# Responsible for compound operational
# signal correlation and converging
# threat behavior analysis.
# =========================================================

from intelligence.correlation_analyzer import (
    analyze_operational_correlation
)

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

from intelligence.confidence_analyzer import(
    analyze_operational_confidence
)

from intelligence.stability_analyzer import (
    analyze_operational_stability
)

from intelligence.health_analyzer import (
    analyze_operational_health
)

from intelligence.threat_pattern_analyzer import (
    analyze_threat_patterns
)

from intelligence.history_analyzer import (
    analyze_historical_patterns
)


# =========================================================
# Adaptive Intelligence Imports
#
# Responsible for operational reflection,
# telemetry weakness analysis, instability
# trend detection, and adaptive evolution
# recommendations.
# =========================================================

from intelligence.adaptive_analyzer import (
    analyze_adaptive_opportunities
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
# Baseline Operational Analysis
#
# Establish recurring telemetry baselines
# and identify dominant operational
# behavior patterns.
#
# Goal:
# Build anomaly awareness foundations.
# =========================================================

baseline = analyze_operational_baseline(
    execution_history
)

print("\n=== OPERATIONAL BASELINE ===\n")

print(
    f"Common Risk: "
    f"{baseline['common_risk']}"
)

print(
    f"Execution Volume: "
    f"{baseline['execution_volume']}"
)

# =========================================================
# Operational Drift Analysis
#
# Compare current telemetry behavior
# against established operational
# baselines.
#
# Goal:
# Detect abnormal operational deviation.
# =========================================================

drift_analysis = analyze_operational_drift(
    execution_history,
    baseline
)

print("\n=== OPERATIONAL DRIFT ===\n")

print(
    f"Drift Detected: "
    f"{drift_analysis['drift_detected']}"
)

if drift_analysis["reasons"]:
    print("\nReasons:\n")

    for reason in drift_analysis["reasons"]:
        print(f"- {reason}")

# =========================================================
# Operational Correlation Analysis
#
# Correlate operational telemetry signals
# to identify compound threat indicators
# and converging operational risk behavior.
#
# Goal:
# Support intelligent escalation analysis.
# =========================================================

correlation_analysis = (
    analyze_operational_correlation(
        execution_history
    )
)

print("\n=== OPERATIONAL CORRELATION ===\n")

print(
    f"Correlation Detected: "
    f"{correlation_analysis['correlation_detected']}"
)

if correlation_analysis["reasons"]:

    print("\nReasons:\n")

    for reason in correlation_analysis["reasons"]:

        print(f"- {reason}")

 # =========================================================
# Operational Confidence Analysis
#
# Evaluate confidence levels associated
# with telemetry interpretation and
# operational conclusions.
#
# Goal:
# Support explainable operational certainty.
# =========================================================

try:

    confidence_analysis = (
        analyze_operational_confidence(
            execution_history
        )
    )

except Exception as error:

    print(
        f"[ERROR] Confidence analyzer failed: "
        f"{error}"
    )

    confidence_analysis = {
        "confidence": "UNKNOWN",
        "reason": (
            "Operational confidence analysis "
            "degraded due to analyzer instability."
        ),
        "details": [
            "Confidence evaluation could not "
            "complete safely."
        ]
    }

print("\n=== OPERATIONAL CONFIDENCE ===\n")

print(
    f"Confidence Level: "
    f"{confidence_analysis['confidence']}"
)

print(
    f"Reason: "
    f"{confidence_analysis['reason']}"
)

if confidence_analysis["details"]:

    print("\nDetails:\n")

    for detail in confidence_analysis["details"]:

        print(f"- {detail}")       

# =========================================================
# Operational Stability Analysis
#
# Evaluate overall operational stability
# conditions across telemetry activity.
#
# Goal:
# Support operational resilience awareness.
# =========================================================

try: 

    stability_analysis = (
        analyze_operational_stability(
            execution_history
        )
    )

except Exception as error: 

    print(
        f"[ERROR] Stability analyzer failed: "
        f"{error}"
    )

    stability_analysis = {
        "stability": "UNKNOWN",
        "stable_executions": 0, 
        "degraded_executions": 0, 
        "reasons": [
            "Operational stability analysis"
            "degraded due to analyzer instability"
        ]
    }

print("\n=== OPERATIONAL STABILITY ===\n")

print(
    f"Stability: "
    f"{stability_analysis['stability']}"
)

print(
    f"\nStable Executions: "
    f"{stability_analysis['stable_executions']}"
)

print(
    f"Degraded Executions: "
    f"{stability_analysis['degraded_executions']}"
)

if stability_analysis["reasons"]:

    print("\nReasons:\n")

    for reason in stability_analysis["reasons"]:

        print(f"- {reason}")

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

try:

    operational_posture = (
        analyze_operational_posture(
            execution_history
        )
    )

except Exception as error:

    print(
        f"[ERROR] Posture analyzer failed: "
        f"{error}"
    )

    operational_posture = {
        "posture": "UNKNOWN",
        "reasons": [
            "Operational posture analysis "
            "degraded due to analyzer instability."
        ]
    }

print("\n=== OPERATIONAL POSTURE ===\n")

print(
    operational_posture["posture"]
)

print("\nReasons:")

for reason in operational_posture["reasons"]:
    print(f"- {reason}")

# =========================================================
# Operational Health Analysis
#
# Evaluate overall operational health
# conditions across telemetry intelligence.
#
# Goal:
# Provide high-level environmental awareness.
# =========================================================

try:

    health_analysis = (
        analyze_operational_health(
            operational_posture,
            confidence_analysis,
            stability_analysis
        )
    )

except Exception as error:

    print(
        f"[ERROR] Health analyzer failed: "
        f"{error}"
    )

    health_analysis = {
        "health": "UNKNOWN",
        "reasons": [
            "Operational health analysis "
            "degraded due to analyzer instability."
        ]
    }
print("\n=== OPERATIONAL HEALTH ===\n")

print(
    f"Health: "
    f"{health_analysis['health']}"
)

if health_analysis["reasons"]:

    print("\nReasons:\n")

    for reason in health_analysis["reasons"]:

        print(f"- {reason}") 

# =========================================================
# Threat Pattern Analysis
#
# Identify recurring HIGH RISK and
# DEGRADED operational behavior that
# may indicate emerging threat activity.
#
# Goal:
# Support behavioral threat awareness.
# =========================================================

try:

    threat_analysis = (
        analyze_threat_patterns(
            execution_history
        )
    )

except Exception as error:

    print(
        f"[ERROR] Threat pattern analyzer failed: "
        f"{error}"
    )

    threat_analysis = {
        "threat_detected": False,
        "threat_count": 0,
        "reasons": [
            "Threat pattern analysis degraded "
            "due to analyzer instability."
        ]
    }

print("\n=== THREAT PATTERN ANALYSIS ===\n")

print(
    f"Threat Detected: "
    f"{threat_analysis['threat_detected']}"
)

print(
    f"Threat Count: "
    f"{threat_analysis['threat_count']}"
)

if threat_analysis["reasons"]:

    print("\nReasons:\n")

    for reason in threat_analysis["reasons"]:

        print(f"- {reason}")   

# =========================================================
# Historical Pattern Analysis
#
# Analyze recurring operational behavior
# across telemetry history to identify
# persistent patterns and trends.
#
# Goal:
# Support long-term operational awareness.
# =========================================================

try:

    historical_analysis = (
        analyze_historical_patterns(
            execution_history
        )
    )

except Exception as error:

    print(
        f"[ERROR] Historical analyzer failed: "
        f"{error}"
    )

    historical_analysis = {
        "patterns_detected": False,
        "patterns": [
            "Historical pattern analysis "
            "degraded due to analyzer instability."
        ]
    }

print("\n=== HISTORICAL PATTERN ANALYSIS ===\n")

print(
    f"Patterns Detected: "
    f"{historical_analysis['patterns_detected']}"
)

if historical_analysis["patterns"]:

    print("\nPatterns:\n")

    for pattern in historical_analysis["patterns"]:

        print(f"- {pattern}")    

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
# Adaptive Intelligence Analysis
#
# Analyze recurring telemetry weaknesses,
# instability patterns, and future
# operational refinement opportunities.
#
# Philosophy:
# Observe.
# Interpret.
# Reflect.
# Evolve.
# =========================================================

try:

    adaptive_insights = (
        analyze_adaptive_opportunities(
            execution_history
        )
    )

except Exception as error:

    print(
        f"[ERROR] Adaptive analyzer failed: "
        f"{error}"
    )

    adaptive_insights = [
        "Adaptive operational analysis "
        "degraded due to analyzer instability."
    ]

print("\n=== ADAPTIVE INTELLIGENCE ===\n")

for insight in adaptive_insights:
    print(f"- {insight}")

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

try:

    escalation_status = analyze_escalation(
        execution_history
    )

except Exception as error:

    print(
        f"[ERROR] Escalation analyzer failed: "
        f"{error}"
    )

    escalation_status = {
        "escalation": "UNKNOWN",
        "reason": (
            "Escalation analysis degraded "
            "due to analyzer instability."
        )
    }

print("\n=== ESCALATION STATUS ===\n")

print(
    f"Escalation Required: "
    f"{escalation_status['escalation']}"
)

print(
    f"Reason: "
    f"{escalation_status['reason']}"
)