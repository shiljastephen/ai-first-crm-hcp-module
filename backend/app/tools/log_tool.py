import json

from app.services.groq_service import llm
from app.prompts.system_prompts import LOG_INTERACTION_PROMPT

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
        LOG_INTERACTION_PROMPT + "\n\n" + user_message
    )

    content = response.content.strip()

    start = content.find("{")
    end = content.rfind("}")

    if start != -1 and end != -1:
        content = content[start:end + 1]

    return json.loads(content)