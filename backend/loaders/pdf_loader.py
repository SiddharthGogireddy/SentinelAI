from pypdf import PdfReader


def extract_pdf_text(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    pdf_path = "sample.pdf"

    try:
        extracted_text = extract_pdf_text(pdf_path)

        print(extracted_text[:1000])

    except FileNotFoundError:
        print("PDF file not found.")