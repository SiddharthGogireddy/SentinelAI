from io import BytesIO
from pypdf import PdfReader

from backend.preprocess.clause_splitter import split_into_clauses


async def extract_pdf_clauses(file):
    """
    Extract clauses and their page numbers from an uploaded PDF.
    """

    contents = await file.read()

    pdf_stream = BytesIO(contents)

    reader = PdfReader(pdf_stream)

    clauses_with_pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text() or ""

        clauses = split_into_clauses(page_text)

        for clause in clauses:
            clauses_with_pages.append({
                "clause": clause,
                "page": page_number
            })

    return clauses_with_pages


async def extract_pdf_text(file) -> str:
    """
    Extract plain text from an uploaded PDF.
    """

    contents = await file.read()

    pdf_stream = BytesIO(contents)

    reader = PdfReader(pdf_stream)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text