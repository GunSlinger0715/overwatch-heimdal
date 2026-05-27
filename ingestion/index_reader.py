# =========================================================
# Heimdal Telemetry Ingestion Layer
#
# Purpose:
# Safely load, normalize, and validate
# operational telemetry execution history
# before intelligence processing begins.
#
# Responsibilities:
# - Load execution telemetry safely
# - Validate telemetry structure
# - Normalize execution entries
# - Enforce ingestion trust boundaries
# - Detect malformed telemetry
# - Support future quarantine routing
#
# Philosophy:
# Intelligence begins with trusted telemetry.
#
# Untrusted telemetry must never compromise
# operational cognition.
#
# Observe.
# Validate.
# Isolate.
# Protect.
# =========================================================

import json
from pathlib import Path

from models.execution_model import Execution

REQUIRED_FIELDS = [
    "timestamp", 
    "endpoint", 
    "score",
    "risk"
]

def load_execution_index(index_path):
    """
    Load the execution index JSON file safely.
    
    Args: 
        index_path (str): Path to execution_index.json
        
    Returns: 
        list: Parsed execution history entries
        """
    try: 
        index_file = Path(index_path)
        if not index_file.exists():
            print(f"[ERROR] Execution index not found: {index_path}")
            return []
        
        with open(index_file, "r", encoding="utf-8") as file:
            execution_history = json.load(file)

        print(f"[INFO] Loaded {len(execution_history)} execution entries.")

        normalized_executions = []

        for entry in execution_history:

            trust_status = "TRUSTED"
            trust_score = 1.0
            validation_issues = []

            for field in REQUIRED_FIELDS:
                if field not in entry:
                    validation_issues.append(f"Missing field: {field}")
                    trust_score -= 0.1

                if not isinstance(entry.get("findings", []), list):
                    validation_issues.append("Findings must be a list.")

                if not isinstance(entry.get("endpoint"), str):
                    validation_issues.append("Endpoint must be a string.")
                    trust_score -= 0.2

                if trust_score < 0.8: 
                    trust_status = "DEGRADED"
                
                if trust_score < 0.5: 
                    trust_status = "SUSPICIOUS"

                trust_score = max(trust_score, 0.0)

        execution = Execution(
            timestamp=entry.get("timestamp"),
            endpoint=entry.get("endpoint"),
            score=entry.get("score"),
            risk=entry.get("risk"),
            current_phase=entry.get("current_phase"),
            stability=entry.get("stability"),
            findings=entry.get("findings", []),
            trust_status=trust_status, 
            trust_score=trust_score, 
            validation_issues=validation_issues
        )

        normalized_executions.append(execution)

        return normalized_executions

    except json.JSONDecodeError: 
        print("[ERROR] Failed to parse exection index JSON.")
        return []

    except Exception as error: 
        print(f"[ERROR] Unexpected error loading execution index: {error}")
        return []