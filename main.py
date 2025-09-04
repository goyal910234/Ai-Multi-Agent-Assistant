from fastapi import FastAPI
from agent_system.orchestrator import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Multi-Agent Assistant is running!"}

@app.get("/ask")
def ask_agent(query: str):
    response = run_agent(query)
    return {"query": query, "response": response}
