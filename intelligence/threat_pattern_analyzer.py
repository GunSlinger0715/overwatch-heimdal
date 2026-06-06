# =========================================================
# Heimdal Threat Pattern Analyzer
#
# Purpose:
# Identify recurring operational behavior
# patterns that may indicate emerging
# threat activity or attack conditions.
#
# Responsibilities:
# - Detect repeated HIGH RISK activity
# - Identify concentrated endpoint targeting
# - Detect recurring degraded stability
# - Support behavioral threat awareness
#
# Philosophy:
# Repeated hostile behavior often reveals
# deeper operational intent.
#
# Observe.
# Correlate.
# Recognize.
# Escalate.
# =========================================================

def analyze_threat_patterns(executions): 

    threat_detected = False
    threat_count = 0
    threat_reasons = []
    
    for execution in executions:
         if (
              execution.risk == "HIGH RISK"
              and 
              execution.stability == "DEGRADED"
         ):
          
            threat_detected = True
            threat_count += 1
    
            threat_reasons.append(
                f"Repeated HIGH RISK and "
                f"DEGRADED activity observed "
                f"for {execution.endpoint}."
            )
    if threat_count > 0:
       
       threat_reasons = [
          (
             f"{threat_count} HIGH RISK and "
             f"DEGRADED execution(s) detected."
          )
       ]


    return {
       "threat_detected": threat_detected, 
       "threat_count": threat_count,
       "reasons": threat_reasons
    }