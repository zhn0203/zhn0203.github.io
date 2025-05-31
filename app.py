from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str

@app.post("/api/search")
async def search(q: Query):
    # Dummy response (to be replaced with real Google, YouTube, ChatGPT API results)
    return [
        {"title": "Example Google Result", "snippet": "Snippet from Google", "link": "https://google.com"},
        {"title": "Example YouTube Video", "snippet": "Snippet from YouTube", "link": "https://youtube.com"},
        {"title": "ChatGPT Summary", "snippet": "AI-generated summary", "link": "#"}
    ]
