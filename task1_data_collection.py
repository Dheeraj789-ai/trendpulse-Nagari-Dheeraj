import requests
import json
import os
import time
from datetime import datetime


# Step 1: Define categories + keywords

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "champiOnship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


# Step 2: Function to assign category

def get_category(title):
    """
    This function checks if any keyword is present in the title
    and returns the corresponding category.
    """
    title = title.lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title:
                return category

    return None



# Step 3: Fetch top story IDs

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

try:
    response = requests.get(url, headers=headers)
    story_ids = response.json()[:500]   # Take first 500 IDs
except Exception as e:
    print("Error fetching top stories:", e)
    story_ids = []



# Step 4: Initialize storage

collected_data = []
category_count = {key: 0 for key in categories.keys()}


# Step 5: Fetch each story
for story_id in story_ids:

    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        res = requests.get(story_url, headers=headers)
        story = res.json()
    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        continue

    # Skip if no valid title
    if not story or "title" not in story:
        continue

    # Assign category
    category = get_category(story["title"])

    # Skip if no category matched
    if category is None:
        continue

    # Limit 25 per category
    if category_count[category] >= 25:
        continue

  
    # Step 6: Extract required fields
 
    data = {
        "post_id": story.get("id"),
        "title": story.get("title"),
        "category": category,
        "score": story.get("score", 0),
        "num_comments": story.get("descendants", 0),
        "author": story.get("by"),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Store data
    collected_data.append(data)
    category_count[category] += 1

  
    # Step 7: Stop when all categories have 25
  
    if all(count >= 25 for count in category_count.values()):
        break

    
    # Step 8: Sleep after each category batch
    
    if sum(category_count.values()) % 25 == 0:
        time.sleep(2)



# Step 9: Save JSON file

# Create folder if not exists
if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(collected_data, f, indent=4)



# Step 10: Print result

print(f"Collected {len(collected_data)} stories. Saved to {filename}")
