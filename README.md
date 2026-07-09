# AI-First CRM HCP Module

An AI-powered CRM module for pharmaceutical sales representatives to efficiently log and manage Healthcare Professional (HCP) interactions using natural language.

The application provides both a structured interaction form and an AI chat assistant powered by LangGraph and Groq LLM.

---

## Features

- AI-powered interaction logging
- AI-assisted interaction editing
- Automatic CRM form population
- AI-generated meeting summaries
- Follow-up suggestions
- Next Best Action recommendations
- Structured interaction storage
- Responsive React UI
- REST API using FastAPI

---

## Tech Stack

### Frontend

- React
- Redux Toolkit
- Axios
- CSS
- Google Inter Font

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL / MySQL
- Pydantic

### AI

- LangGraph
- LangChain
- Groq API
- LLM (OpenAI GPT OSS / Groq supported model)

---

## LangGraph Tools

### 1. Log Interaction Tool

Extracts structured CRM information from natural language and populates the interaction form.

### 2. Edit Interaction Tool

Updates only the requested fields while preserving all other interaction data.

### 3. Summary Tool

Generates a concise summary of the interaction.

### 4. Follow-up Tool

Suggests appropriate follow-up actions for the sales representative.

### 5. Recommendation Tool

Provides AI-powered next best action recommendations.

---

## Project Structure

```
AI-CRM-HCP
│
├── frontend
│   ├── src
│   ├── components
│   ├── features
│   ├── api
│   └── styles
│
├── backend
│   ├── app
│   │   ├── graph
│   │   ├── models
│   │   ├── routers
│   │   ├── prompts
│   │   ├── services
│   │   ├── tools
│   │   └── schemas
│   │
│   └── main.py
│
└── README.md
```

---

## How It Works

1. User describes an HCP interaction in the AI chat.
2. LangGraph detects the user's intent.
3. The appropriate AI tool is selected.
4. Groq LLM processes the request.
5. Structured CRM data is generated.
6. Redux updates the interaction form.
7. Interaction is stored in the database.

---

## Supported AI Intents

- Log Interaction
- Edit Interaction
- Generate Summary
- Suggest Follow-up
- Recommend Next Best Action

---

## API Endpoints

### AI

```
POST /ai/chat
```

### Interactions

```
GET /interactions
POST /interactions
PUT /interactions/{id}
DELETE /interactions/{id}
```

---

## Installation

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Environment Variables

Create a `.env` file inside the backend directory.

```
DATABASE_URL=your_database_url
GROQ_API_KEY=your_api_key
MODEL_NAME=your_model_name
```

---

## Future Improvements

- Authentication & Authorization
- Multi-user CRM
- HCP Search
- Analytics Dashboard
- Email Integration
- Calendar Integration
- Voice Interaction Logging

---

## Author

**Shilja S**

Python Full Stack Developer

Built as part of the AI-First CRM HCP Module Technical Assignment.