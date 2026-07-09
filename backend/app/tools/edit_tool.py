from app.services.groq_service import llm
from app.prompts.system_prompts import EDIT_INTERACTION_PROMPT
import json


def edit_interaction(current_data: dict, instruction: str) -> dict:
    """
    Update an existing CRM interaction using a natural language instruction.
    Only the fields mentioned by the user should be modified.
    """

    prompt = f"""
{EDIT_INTERACTION_PROMPT}

Current CRM Interaction:

{json.dumps(current_data, indent=2)}

User Instruction:

{instruction}
"""

    response = llm.invoke(prompt)

    try:
        updated_data = json.loads(response.content)
        return updated_data
    except Exception:
        # If parsing fails, return the original data
        return current_data