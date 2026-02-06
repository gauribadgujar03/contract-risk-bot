def generate_summary(risk_level, total_clauses):
    return f"""
    This contract contains {total_clauses} major clauses.
    Overall risk level is {risk_level}.
    Review high-risk clauses carefully before signing.
    """
