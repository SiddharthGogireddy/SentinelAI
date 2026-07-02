from bs4 import BeautifulSoup


def extract_html_text(html_path: str) -> str:
    """
    Extracts readable text from an HTML file.
    """

    with open(html_path, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    # Remove scripts and styles
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    return text
if __name__ == "__main__":

    path = "ai/datasets/raw/Discord/privacy_policy.html"

    text = extract_html_text(path)

    print(text[:1000])