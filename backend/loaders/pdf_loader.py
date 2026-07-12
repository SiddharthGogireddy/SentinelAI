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

async def extract_pdf_clauses(file):

    contents = await file.read()

    pdf_stream = BytesIO(contents)

    reader = PdfReader(pdf_stream)

    clauses_with_pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text() or ""

        clauses = split_into_clauses(page_text)

        for item in clauses:

            if isinstance(item, dict):
                clause = item["clause"]
                page = item["page"]
        else:
            clause = item
            page = None

            
    return clauses_with_pages