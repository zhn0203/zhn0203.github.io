import os
import requests

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_google(query):
    url = f"https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google"
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = []
    for result in data.get("organic_results", []):
        results.append({
            "title": result.get("title"),
            "snippet": result.get("snippet"),
            "link": result.get("link")
        })
    return results
