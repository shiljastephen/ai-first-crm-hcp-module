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
        SYSTEM_PROMPT + "\n\n" + user_message
    )
    print("LLM Response:")
    print(response.content)
    return json.loads(response.content)