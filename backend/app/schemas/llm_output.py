from pydantic import BaseModel


class InteractionExtraction(BaseModel):

    hcp_name: str=""
    interaction_type: str=""
    interaction_date: str=""
    interaction_time: str=""
    attendees: str=""
    topics_discussed: str=""
    materials_shared: str=""
    summary: str=""
    sentiment: str=""
    follow_up: str=""