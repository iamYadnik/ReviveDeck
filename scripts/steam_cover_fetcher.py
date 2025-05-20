import os
import json
import requests

# NOTE: Replace with your SteamGridDB API key
API_KEY = "YOUR_STEAMGRIDDB_API_KEY"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
CACHE_DIR = "assets/covers"

def fetch_cover(app_id):
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"{app_id}.jpg")
    if os.path.exists(cache_path):
        print(f"✅ Cover already cached for AppID {app_id}")
        return cache_path

    try:
        print(f"🔍 Fetching cover for AppID: {app_id}")
        response = requests.get(
            f"https://www.steamgriddb.com/api/v2/grids/game/{app_id}?dimensions=600x900",
            headers=HEADERS
        )
        data = response.json()
        if "data" not in data or len(data["data"]) == 0:
            print("❌ No cover found.")
            return None

        img_url = data["data"][0]["url"]
        img_data = requests.get(img_url).content
        with open(cache_path, "wb") as f:
            f.write(img_data)
        print(f"✅ Cover saved to {cache_path}")
        return cache_path
    except Exception as e:
        print(f"❌ Error fetching cover: {e}")
        return None

if __name__ == "__main__":
    sample_id = input("Enter Steam AppID to fetch cover: ").strip()
    fetch_cover(sample_id)