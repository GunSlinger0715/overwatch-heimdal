from black_cells.quarantine_manager import (
    should_quarantine,
    quarantine_telemetry
)

from models.execution_model import Execution


test_execution = Execution(
    timestamp="2026-05-29 06:45:00",
    endpoint="/api/test",
    score=15,
    risk="HIGH",
    current_phase="TESTING",
    stability="DEGRADED",
    findings=["Malformed telemetry detected."],
    trust_status="SUSPICIOUS",
    trust_score=0.2,
    validation_issues=[
        "Telemetry structure inconsistency detected."
    ]
)
if should_quarantine(test_execution):

    quarantine_telemetry(
        test_execution,
        "Automatic quarantine evaluation triggered."
    )

else:

    print(
        "[BLACK CELLS] "
        "Telemetry cleared operational review."
    )