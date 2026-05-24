import json
from pathlib import Path

from models.execution_model import Execution

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

            execution = Execution(
            timestamp=entry.get("timestamp"),
            endpoint=entry.get("endpoint"),
            score=entry.get("score"),
            risk=entry.get("risk"),
            current_phase=entry.get("current_phase"),
            stability=entry.get("stability"),
            findings=entry.get("findings", [])
        )

        normalized_executions.append(execution)

        return normalized_executions

    except json.JSONDecodeError: 
        print("[ERROR] Failed to parse exection index JSON.")
        return []

    except Exception as error: 
        print(f"[ERROR] Unexpected error loading execution index: {error}")
        return []