import re


def extract_text(text: str) -> str:
    

    if not text:
        return ""

    # Remove leading/trailing whitespace
    text = text.strip()

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace multiple blank lines with a single blank line
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text

