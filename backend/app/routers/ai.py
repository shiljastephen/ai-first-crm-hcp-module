from pydantic import BaseModel
from fastapi import APIRouter
from app.schemas.ai import ChatRequest
from app.graph.workflow import graph

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "user_message": request.message,
            "interaction_data": request.current_interaction
        }
    )

    return result.get("response", {})