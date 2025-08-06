import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_google_news(query):
    params = {
        "engine": "google",
        "q": query,
        "gl": "us",
        "api_key": SERPAPI_KEY,
        "tbm": "nws"
    }
    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    news_items = data.get("news_results", [])
    results = []

    for item in news_items:
        title = item.get("title", "No title")
        source = item.get("source", "Unknown source")
        date = item.get("date", "Unknown date")
        snippet = item.get("snippet", "No summary available.")

        formatted = (
            f" **{title}**"
            f" {date} | {source}"
            f"{snippet}"
        )
        results.append(formatted)

    print(results)

    return "\n\n".join(results)