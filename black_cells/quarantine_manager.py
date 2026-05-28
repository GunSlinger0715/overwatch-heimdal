# =========================================================
# OVERWATCH Black Cells
#
# Purpose:
# Isolate uncertain operational telemetry
# from Heimdal's cognition pipeline.
#
# Responsibilities:
# - Preserve cognition integrity
# - Isolate suspicious telemetry
# - Maintain operational evidence
# - Support future adjudication workflows
#
# Philosophy:
# Uncertain telemetry should never
# poison operational cognition.
#
# Isolate.
# Preserve.
# Observe.
# Judge.
# =========================================================

# =========================================================
# Black Cells Imports
#
# Responsible for operational telemetry
# isolation persistence and containment.
# =========================================================
import json
from pathlib import Path

# =========================================================
# Black Cells Storage Configuration
#
# Defines operational isolation storage
# locations for quarantined telemetry.
# =========================================================
BLACK_CELLS_PATH = (
    Path(__file__).parent / "black_cells.json"
)

# =========================================================
# Telemetry Isolation Functions
#
# Responsible for safely isolating
# uncertain operational telemetry.
# =========================================================

# =========================================================
# Quarantine Evaluation Functions
#
# Responsible for determining whether
# telemetry should be isolated safely.
# =========================================================
def should_quarantine(execution):
    """
    Determine whether telemetry should
    be isolated within the Black Cells.
    """

    if execution.trust_score <= 0.3:
        return True

    if execution.trust_status == "SUSPICIOUS":
        return True

    if len(execution.validation_issues) > 0:
        return True

    return False

# =========================================================
# Quarantine Evaluation Functions
#
# Responsible for determining whether
# telemetry should be isolated safely.
# =========================================================
def should_quarantine(execution):
    """
    Determine whether telemetry should
    be isolated within the Black Cells.
    """

    if execution.trust_score <= 0.3:
        return True

    if execution.trust_status == "SUSPICIOUS":
        return True

    if len(execution.validation_issues) > 0:
        return True

    return False

def quarantine_telemetry(
    execution,
    quarantine_reason
):
    """
    Isolate suspicious or uncertain telemetry
    safely within the Black Cells.
    """

    try:

        if BLACK_CELLS_PATH.exists():

            with open(
                BLACK_CELLS_PATH,
                "r",
                encoding="utf-8"
            ) as file:

                quarantined_data = json.load(file)

        else:
            quarantined_data = []

        quarantined_entry = {
            "timestamp": execution.timestamp,
            "endpoint": execution.endpoint,
            "trust_score": execution.trust_score,
            "trust_status": execution.trust_status,
            "validation_issues": (
                execution.validation_issues
            ),
            "quarantine_reason": quarantine_reason
        }

        quarantined_data.append(
            quarantined_entry
        )

        with open(
            BLACK_CELLS_PATH,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                quarantined_data,
                file,
                indent=4
            )

        print(
            "[BLACK CELLS] "
            "Telemetry isolated successfully."
        )

    except Exception as error:

        print(
            "[BLACK CELLS ERROR] "
            f"Failed to isolate telemetry: "
            f"{error}"
        )
