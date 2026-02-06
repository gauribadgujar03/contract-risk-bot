import streamlit as st

from core.risk_engine import (
    calculate_clause_risk,
    classify_risk,
    contract_risk_summary,
    explain_clause
)

st.title("Contract Risk Analysis Bot")

contract_text = """
Payment shall be made within 30 days.
Late payment attracts penalty.
The vendor is not liable for indirect damages.
"""

clauses = [c.strip() for c in contract_text.split('.') if c.strip()]
scores = []

for i, clause in enumerate(clauses, 1):
    score = calculate_clause_risk(clause)
    risk = classify_risk(score)
    scores.append(score)

    with st.expander(f"Clause {i} | Risk: {risk} | Score: {score}/100"):
        st.write(clause)
        st.info(explain_clause(clause))

contract_risk = contract_risk_summary(scores)

st.subheader("Overall Contract Risk")
st.success(contract_risk)
