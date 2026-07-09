from app.services.groq_service import llm

PROMPT = """
Summarize the interaction in 2-3 professional CRM sentences.
"""


def summarize(text):

    response = llm.invoke(
        PROMPT + "\n\n" + text
    )

    return response.content