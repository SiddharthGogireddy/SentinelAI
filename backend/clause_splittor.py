import re


def split_into_clauses(text: str) -> list[str]:
    
    if not text:
        return []

    
    clauses = re.split(r"\n\s*\n", text)

    
    clauses = [c.strip() for c in clauses if c.strip()]

    return clauses