from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get Google Search API and Google Custom Web Search keys from .env file
google_search_api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
google_cse_id = os.getenv('GOOGLE_CSE_ID')

if not google_search_api_key or not google_cse_id:
    raise ValueError("Google API keys not found in .env file")

def google_search(query):
    """Search the internet using Google Search."""
    service = build("customsearch", "v1", developerKey=google_search_api_key)
    res = service.cse().list(q=query, cx=google_cse_id).execute()
    results = [item['title'] for item in res['items']]
    return {"context": ", ".join(results), "titles": results}

def google_custom_search(query):
    """Perform a custom web search using Google Custom Web Search."""
    service = build("customsearch", "v1", developerKey=google_search_api_key)
    res = service.cse().list(q=query, cx=google_cse_id).execute()
    results = [item['snippet'] for item in res['items']]
    return {"context": ", ".join(results)}
