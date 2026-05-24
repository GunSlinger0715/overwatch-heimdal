def get_high_risk_executions(executions):
    """
    Return all HIGH RISK executions.
    """

    high_risk = []

    for execution in executions:
        if execution.risk == "HIGH RISK":
            high_risk.append(execution)

    return high_risk

def get_degraded_executions(executions): 
    """
    Return all DEGRADED executions.
    """

    degraded = []

    for execution in executions:
        if execution.stability == "DEGRADED":
            degraded.append(execution)

    return degraded

def get_executions_by_endpoint(executions, endpoint):
    """
    Return executions matching a specific endpoint.
    """

    matching_executions = []

    for execution in executions:
        if execution.endpoint == endpoint:
            matching_executions.append(execution)

    return matching_executions