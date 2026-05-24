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
        findings
    ):
        self.timestamp = timestamp
        self.endpoint = endpoint
        self.score = score
        self.risk = risk
        self.current_phase = current_phase
        self.stability = stability
        self.findings = findings

    def summary(self):
        return (
            f"[{self.timestamp}] "
            f"{self.endpoint} | "
            f"Risk: {self.risk} | "
            f"Stability: {self.stability}"
        )