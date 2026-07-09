from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.models import *
from app.routers import interaction_router
from app.routers.ai import router as ai_router

app = FastAPI(
    title="AI CRM HCP Module",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(interaction_router)
app.include_router(ai_router)


@app.get("/")
def home():
    return {
        "message": "AI CRM HCP Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }