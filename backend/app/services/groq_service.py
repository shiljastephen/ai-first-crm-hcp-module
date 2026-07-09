from langchain_groq import ChatGroq
from app.core.config import *
from app.core.config import GROQ_API_KEY
from app.core.config import MODEL_NAME

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)