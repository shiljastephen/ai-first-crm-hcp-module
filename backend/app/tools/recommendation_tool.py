from app.services.groq_service import llm

PROMPT = """
Recommend the next best sales action.

Return one recommendation only.
"""


def recommendation(text):

    response = llm.invoke(
        PROMPT + "\n\n" + text
    )

    return response.content