import re



def split_into_clauses(text: str) -> list[str]:
    """
    Splits a privacy policy into meaningful clauses.
    """

    if not text:
        return []

    text = text.replace("\r\n", "\n")

    paragraphs = re.split(r"\n\s*\n", text)

    clauses = []

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        # Skip headings
        if is_heading(paragraph):
            continue

        # Split long paragraphs into sentences
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)

        for sentence in sentences:

            sentence = sentence.strip()

            if len(sentence) > 15:
                clauses.append(sentence)

    return clauses

    return clauses
def is_heading(text: str) -> bool:
    text = text.strip()

    # Empty
    if not text:
        return True

    # Most headings are short
    if len(text.split()) <= 5:

        # Headings usually don't contain commas
        if "," not in text:

            # Headings usually don't start with these words
            starts = (
                "We ",
                "You ",
                "Your ",
                "If ",
                "For ",
                "This ",
                "These ",
                "Those ",
                "When ",
                "Where ",
                "How ",
                "Why ",
                "In ",
                "On ",
                "At "
            )

            if not text.startswith(starts):
                return True

    return False