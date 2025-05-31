import os
import requests

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube(query):
    url = f"https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "maxResults": 5
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = []
    for item in data.get("items", []):
        snippet = item["snippet"]
        video_id = item["id"]["videoId"]
        results.append({
            "title": snippet["title"],
            "snippet": snippet["description"],
            "link": f"https://www.youtube.com/watch?v={video_id}"
        })
    return results
