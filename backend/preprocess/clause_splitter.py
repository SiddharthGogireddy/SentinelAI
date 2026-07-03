import re


def is_heading(text: str) -> bool:
    text = text.strip()

    if not text:
        return True

    # Remove trailing colon or period
    cleaned = text.rstrip(".:")

    words = cleaned.split()

    # Headings are usually short
    if len(words) <= 5:

        # They usually don't contain commas
        if "," not in cleaned:

            # They usually don't begin like sentences
            sentence_starters = (
                "We",
                "You",
                "Your",
                "Our",
                "This",
                "These",
                "Those",
                "If",
                "For",
                "When",
                "While",
                "Because",
                "Since",
                "To"
            )

            if not cleaned.startswith(sentence_starters):
                return True

    return False


def split_into_clauses(text: str) -> list[str]:
    """
    Splits a privacy policy into meaningful clauses.
    """

    text = text.replace("\r\n", "\n")

    paragraphs = re.split(r"\n\s*\n", text)

    clauses = []

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if is_heading(paragraph):
            continue

        clauses.append(paragraph)

    return clauses