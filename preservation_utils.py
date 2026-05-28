# =========================================================
# Heimdal Preservation Utilities
#
# Purpose:
# Preserve operational continuity during
# degraded, malformed, or unstable
# telemetry conditions.
#
# Responsibilities:
# - Safe telemetry extraction
# - Graceful degradation support
# - Preservation fallback handling
# - Operational resilience protection
#
# Philosophy:
# Operational cognition should degrade
# gracefully, not collapse completely.
#
# Preserve.
# Stabilize.
# Continue.
# =========================================================

# =========================================================
# Safe Extraction Functions
#
# Responsible for safely retrieving
# telemetry attributes while preserving
# operational continuity.
# =========================================================
def safe_extract(
    execution,
    attribute,
    default=None
):
    """
    Safely extract telemetry attributes
    without collapsing operational flow.
    """

    try:

        value = getattr(
            execution,
            attribute,
            default
        )

        if value is None:
            return default

        return value

    except Exception:

        return default