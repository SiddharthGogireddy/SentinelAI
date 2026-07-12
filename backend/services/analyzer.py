from backend.loaders.text_loader import load_text
from backend.preprocess.clause_splitter import split_into_clauses
from backend.annotation.label_suggester import suggest_labels
from backend.risk.risk_engine import build_alert

def analyze_text(text: str) -> dict:
    """
    Analyze plain text and return detected permissions and risks.
    """

    clauses = split_into_clauses(text)

    results = []

    high = 0
    medium = 0
    low = 0

    for clause in clauses:

        labels = suggest_labels(clause)

        alerts = build_alert(labels,evidence=clause)
       
       

        for alert in alerts:
            level = alert.get("level", "").lower()

            if level == "high":
                high += 1
            elif level == "medium":
                medium += 1
            elif level == "low":
                low += 1

        results.append({
            "clause": clause,
            
            "labels": labels,
            "alerts": alerts
            
            
        })

    return {
        "total_clauses": len(clauses),
        "results": results,
        "summary": {
            "high": high,
            "medium": medium,
            "low": low
        }
    }


def analyze_txt(file_path: str) -> dict:
    """
    Analyze a text file.
    """

    text = load_text(file_path)

    return analyze_text(text)
def analyze_pdf_clauses(clauses_with_pages):

    results = []

    high = medium = low = 0

    for item in clauses_with_pages:

        clause = item["clause"]
        page = item["page"]

        labels = suggest_labels(clause)

        alerts = build_alert(
            labels,
            evidence=clause
            
        )
        for alert in alerts:
            alert["page"] = page

        for alert in alerts:
            level = alert["level"].lower()

            if level == "high":
                high += 1
            elif level == "medium":
                medium += 1
            elif level == "low":
                low += 1

        results.append({
            "clause": clause,
            "page": page,
            "labels": labels,
            "alerts": alerts
        })

    return {
        "total_clauses": len(results),
        "results": results,
        "summary": {
            "high": high,
            "medium": medium,
            "low": low
        }
    }