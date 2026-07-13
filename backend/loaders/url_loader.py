import requests
import trafilatura


def load_url(url: str) -> str:
    """
    Extract main content from a webpage.
    """

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    response.raise_for_status()

    downloaded = response.text

    extracted = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False
    )

    return extracted or ""