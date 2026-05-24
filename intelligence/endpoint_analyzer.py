def analyze_endpoint_activity(executions):
    """
    Analyze recurring endpoint activity.
    """

    endpoint_counts = {}

    for execution in executions:

        endpoint = execution.endpoint

        if endpoint not in endpoint_counts:
            endpoint_counts[endpoint] = 0

        endpoint_counts[endpoint] += 1

    return endpoint_counts