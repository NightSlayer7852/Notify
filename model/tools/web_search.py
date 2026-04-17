import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
client = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))

def search_web(query, max_results = 5):
    try:
        response = client.search(
            query = query,
            search_depth = "advanced",
            max_results = max_results
        )
        results = []
        for r in response.get("results", []):
            results.append({
                "title" : r.get("title"),
                "url" : r.get("url"),
                "content" : r.get("content")
            })
        return results
    except Exception as e:
        return f"Error: {str(e)}"