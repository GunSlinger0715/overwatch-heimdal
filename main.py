from queries.telemetry_queries import (
    get_high_risk_executions,
    get_degraded_executions,
    get_executions_by_endpoint
)
from ingestion.index_reader import load_execution_index
INDEX_PATH = "execution_index.json"


execution_history = load_execution_index(INDEX_PATH)
high_risk_executions = get_high_risk_executions(execution_history)

high_risk_executions = get_high_risk_executions(execution_history)

print("\n=== HIGH RISK EXECUTIONS ===\n")

for execution in high_risk_executions:
    print(execution.summary())

degraded_executions = get_degraded_executions(execution_history)

print("\n=== DEGRADED EXECUTIONS ===\n")

for execution in degraded_executions: 
    print(execution.summary())

endpoint_executions = get_executions_by_endpoint(
    execution_history,
    "GET /invalid-endpoint"
)

print("\n=== ENDPOINT EXECUTIONS ===\n")

for execution in endpoint_executions:
    print(execution.summary())