from typing import TypedDict, Optional, Any

class CRMState(TypedDict):
    user_message: str
    intent: Optional[str]
    interaction_data: Optional[dict[str, Any]]
    response: Optional[dict[str, Any]]