from app.services.groq_service import llm

PROMPT = """
Read the conversation.

Return ONLY the follow-up action.
"""


def followup(text):

    response = llm.invoke(
        PROMPT + "\n\n" + text
    )

    return response.content