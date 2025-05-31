from fastapi import APIRouter
from pydantic import BaseModel
from services.google_search import search_google
from services.youtube_search import search_youtube
from services.chatgpt_summary import get_summary

router = APIRouter()

class Query(BaseModel):
    query: str

@router.post("/api/search")
async def search(q: Query):
    google_results = search_google(q.query)
    youtube_results = search_youtube(q.query)
    chatgpt_result = get_summary(q.query)

    return {
        "google": google_results,
        "youtube": youtube_results,
        "chatgpt": chatgpt_result
    }
