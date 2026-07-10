from langgraph.graph import StateGraph, END
from app.graph.state import CRMState
from app.services.groq_service import llm
from app.tools.log_tool import log_interaction
from app.tools.edit_tool import edit_interaction
from app.tools.summary_tool import summarize
from app.tools.followup_tool import followup
from app.tools.recommendation_tool import recommendation

def detect_intent(state: CRMState):

    message = state["user_message"]

    prompt = f"""
You are an intent classifier.

Classify the user's request into exactly ONE intent.

Rules:

- log → User is describing or recording a doctor interaction or meeting.
- edit → User wants to modify an existing interaction.
- summary → User asks for a summary.
- followup → User asks ONLY for follow-up suggestions.
- recommendation → User asks for recommendations or next best actions.

If the user is describing a meeting with an HCP, ALWAYS return:

log

Return ONLY one word.

User:

{message}
"""

    response = llm.invoke(
        [
            (
                "system",
                "You are an intent classification assistant."
            ),
            (
                "human",
                prompt
            )
        ]
    )
    intent = response.content.strip().lower()

    return {
        "intent": intent
    }

def log_node(state: CRMState):

    result = log_interaction(
        state["user_message"]
    )

    state["response"] = {
        "tool": "log",
        "data": result
    }

    return state

def summary_node(state: CRMState):

    state["response"] = {
        "tool": "summary",
        "summary": summarize(state["user_message"])
    }

    return state

def followup_node(state: CRMState):

    state["response"] = {
        "tool": "followup",
        "follow_up": followup(state["user_message"])
    }

    return state

def recommendation_node(state: CRMState):

    state["response"] = {
        "tool": "recommendation",
        "recommendation": recommendation(state["user_message"])
    }

    return state

def edit_node(state: CRMState):

    result = edit_interaction(
        state["interaction_data"],
        state["user_message"]
    )

    state["response"] = {
        "tool": "edit",
        "data": result
    }

    return state

def route(state: CRMState):

    return state.get("intent", "log")

builder = StateGraph(CRMState)

builder.add_node("intent", detect_intent)

builder.add_node("log", log_node)

builder.add_node("edit", edit_node)

builder.add_node("summary", summary_node)

builder.add_node("followup", followup_node)

builder.add_node("recommendation", recommendation_node)

builder.set_entry_point("intent")

builder.add_conditional_edges(
    "intent",
    route,
    {
        "log": "log",
        "edit": "edit",
        "summary": "summary",
        "followup": "followup",
        "recommendation": "recommendation"
    }
)

builder.add_edge("log", END)

builder.add_edge("edit", END)

builder.add_edge("summary", END)

builder.add_edge("followup", END)

builder.add_edge("recommendation", END)

graph = builder.compile()