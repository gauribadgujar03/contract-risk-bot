def explain_clause(clause: str) -> str:
    return f"This clause may introduce legal or financial risk: '{clause}'"

CLAUSE_WEIGHTS = {
    "penalty": 30,
    "indemnity": 35,
    "termination": 25,
    "non-compete": 30,
    "ip": 25,
    "arbitration": 15,
    "auto-renew": 20
}

AMBIGUOUS_TERMS = [
    "reasonable",
    "best efforts",
    "sole discretion",
    "as determined by",
    "material breach"
]

UNILATERAL_TERMS = [
    "at any time",
    "without notice",
    "solely",
    "exclusive right"
]

DURATION_TERMS = [
    "lock-in",
    "auto-renew",
    "minimum term"
]

FINANCIAL_TERMS = [
    "unlimited liability",
    "indemnify",
    "penalty",
    "liquidated damages"
]

def detect_clause_type(clause):
    clause = clause.lower()
    for key in CLAUSE_WEIGHTS:
        if key in clause:
            return key
    return "general"

def calculate_clause_risk(clause):
    score = 0
    clause_lower = clause.lower()

    # Clause Type Risk
    clause_type = detect_clause_type(clause)
    score += CLAUSE_WEIGHTS.get(clause_type, 5)

    # Ambiguity Risk
    ambiguity_hits = sum(1 for term in AMBIGUOUS_TERMS if term in clause_lower)
    score += ambiguity_hits * 5

    # Unilateral Control Risk
    unilateral_hits = sum(1 for term in UNILATERAL_TERMS if term in clause_lower)
    score += unilateral_hits * 10

    # Financial Exposure Risk
    if any(term in clause_lower for term in FINANCIAL_TERMS):
        score += 20

    # Duration Risk
    if any(term in clause_lower for term in DURATION_TERMS):
        score += 10

    # Jurisdiction Risk
    if "jurisdiction" in clause_lower or "governing law" in clause_lower:
        if "india" not in clause_lower:
            score += 15

    # Cap score
    return min(score, 100)

def classify_risk(score):
    if score >= 66:
        return "High"
    elif score >= 31:
        return "Medium"
    return "Low"

def contract_risk_summary(clause_scores):
    avg_score = sum(clause_scores) / len(clause_scores)

    if avg_score >= 60:
        return "High"
    elif avg_score >= 30:
        return "Medium"
    return "Low"
