from fastapi import APIRouter, UploadFile, File
from backend.loaders.pdf_loader import extract_pdf_clauses
from backend.services.analyzer import analyze_pdf_clauses, analyze_text

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    clauses = await extract_pdf_clauses(file)

    result = analyze_pdf_clauses(clauses)

    return {
        "success": True,
        "data": result
    }