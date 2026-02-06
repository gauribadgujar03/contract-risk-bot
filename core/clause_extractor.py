import re

def extract_clauses(text):
    clauses = re.split(r"\n\s*\d+[\.\)]\s*", text)
    return [c.strip() for c in clauses if len(c.strip()) > 50]
