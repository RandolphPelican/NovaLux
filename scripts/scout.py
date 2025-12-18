import requests
from bs4 import BeautifulSoup
import os

# Context: Searching for the "Fusion" of humanity and AI
SEARCH_QUERY = "AI+human+future+spirituality+crisis"
RSS_URL = f"https://news.google.com/rss/search?q={SEARCH_QUERY}&hl=en-US&gl=US&ceid=US:en"

def gather_context():
    print("Deacon is scouting the digital wilderness...")
    try:
        response = requests.get(RSS_URL)
        soup = BeautifulSoup(response.content, features="xml")
        items = soup.find_all('item')[:5] # Grab top 5 news items
        
        headlines = [f"- {item.title.text}" for item in items]
        context_blob = "\n".join(headlines)
        
        # Ensure the docs folder exists
        if not os.path.exists("docs"):
            os.makedirs("docs")

        with open("docs/sacred_context.txt", "w") as f:
            f.write(context_blob)
            
        print("Success: Intelligence saved to docs/sacred_context.txt")
    except Exception as e:
        print(f"Scout Error: {e}")

if __name__ == "__main__":
    gather_context()
