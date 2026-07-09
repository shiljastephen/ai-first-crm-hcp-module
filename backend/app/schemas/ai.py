from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):

    message: str

    current_interaction: dict | None = None