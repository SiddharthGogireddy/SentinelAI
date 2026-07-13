from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.loaders.url_loader import load_url
from backend.services.analyzer import analyze_text

router = APIRouter()


class URLRequest(BaseModel):
    url: str


@router.post("/url")
async def analyze_url(request: URLRequest):

    if not request.url.strip():
        raise HTTPException(
            status_code=400,
            detail="URL cannot be empty."
        )

    try:
        text = load_url(request.url)

        result = analyze_text(text, source=request.url)

        return {
            "success": True,
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )