from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.services.analyzer import analyze_text


router = APIRouter()


class AnalyzeRequest(BaseModel):
    text: str


@router.post("/analyze")
async def analyze(request: AnalyzeRequest):
    """
    Analyze Terms of Service or Privacy Policy text.
    """

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Input text cannot be empty."
        )

    try:
        result = analyze_text(request.text)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )