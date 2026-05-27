# =========================================================
# Heimdal Execution Intelligence Model
#
# Purpose:
# Define the normalized operational
# execution structure used throughout
# Heimdal's intelligence pipeline.
#
# Responsibilities:
# - Store normalized telemetry data
# - Preserve operational execution context
# - Support layered intelligence analysis
# - Carry telemetry trust metadata
# - Enable analyzer interoperability
#
# Philosophy:
# Structured operational context enables
# reliable intelligence synthesis.
#
# Normalize.
# Preserve.
# Interpret.
# Correlate.
# =========================================================

class Execution:
    """
    Represents a single telemetry execution record.
    """

    def __init__(
        self,
        timestamp,
        endpoint,
        score,
        risk,
        current_phase,
        stability,
        findings, 
        trust_status, 
        trust_score, 
        validation_issues
    ):
        self.timestamp = timestamp
        self.endpoint = endpoint
        self.score = score
        self.risk = risk
        self.current_phase = current_phase
        self.stability = stability
        self.findings = findings
        self.trust_status = trust_status
        self.trust_score = trust_score
        self.validation_issues = validation_issues
        
    def summary(self):
        return (
            f"[{self.timestamp}] "
            f"{self.endpoint} | "
            f"Risk: {self.risk} | "
            f"Stability: {self.stability}"
        )