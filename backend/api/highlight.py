from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
import tempfile
import os

from backend.loaders.pdf_loader import extract_pdf_clauses
from backend.services.analyzer import analyze_pdf_clauses
from backend.services.pdf_highlighter import highlight_pdf

router = APIRouter()


@router.post("/highlight")
async def highlight(file: UploadFile = File(...)):

    temp_input = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    )

    contents = await file.read()

    temp_input.write(contents)
    temp_input.close()

    file.file.seek(0)

    clauses = await extract_pdf_clauses(file)

    analysis = analyze_pdf_clauses(
        clauses
    )

    output_path = temp_input.name.replace(
        ".pdf",
        "_highlighted.pdf"
    )

    highlight_pdf(
        temp_input.name,
        output_path,
        analysis["results"]
    )

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="highlighted_policy.pdf"
    )