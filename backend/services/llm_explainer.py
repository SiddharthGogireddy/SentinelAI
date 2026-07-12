import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"


def explain_clause(clause: str, labels: list[str]) -> str:

    prompt = f"""
You are an AI privacy policy analyst.

Clause:
{clause}

Detected permissions:
{", ".join(labels)}

Explain:
1. Why this permission was flagged.
2. Whether this permission is common.
3. What users should be aware of.

Respond in less than 80 words.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=60,
    )

    response.raise_for_status()

    return response.json()["response"].strip()


