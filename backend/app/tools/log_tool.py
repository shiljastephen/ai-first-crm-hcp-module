import json

from app.services.groq_service import llm


SYSTEM_PROMPT = """
You are an AI CRM assistant.

Read the conversation.

Extract structured CRM information.

Return ONLY valid JSON.

{
 "hcp_name":"",
 "interaction_type":"",
 "interaction_date":"",
 "interaction_time":"",
 "attendees":"",
 "topics_discussed":"",
 "materials_shared":"",
 "summary":"",
 "sentiment":"",
 "follow_up":""
}
"""


def log_interaction(user_message: str):

    response = llm.invoke(
        SYSTEM_PROMPT + "\n\n" + user_message
    )

    return json.loads(response.content)