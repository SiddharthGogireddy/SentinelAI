from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.llm_explainer import explain_clause

router = APIRouter()


class ExplainRequest(BaseModel):
    clause: str
    labels: list


@router.post("/explain")
async def explain(request: ExplainRequest):

    explanation = explain_clause(
        request.clause,
        request.labels
    )

    return {
        "success": True,
        "explanation": explanation
    }