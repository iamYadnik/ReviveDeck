
import os
import json
import requests

METADATA_FILE = "steam_games_metadata.json"
CACHE_DIR = "cache/images"

def download_image(url, dest_path):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(dest_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"✅ Cached: {dest_path}")
        else:
            print(f"❌ Failed to download {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")

def cache_images():
    if not os.path.exists(METADATA_FILE):
        print(f"❌ Metadata file not found: {METADATA_FILE}")
        return

    with open(METADATA_FILE, "r") as f:
        metadata = json.load(f)

    os.makedirs(CACHE_DIR, exist_ok=True)

    for game_name, info in metadata.items():
        img_url = info.get("header_image")
        if not img_url:
            print(f"⚠️ No image URL for: {game_name}")
            continue

        filename = f"{game_name.replace(' ', '_').replace('/', '_')}.jpg"
        dest_path = os.path.join(CACHE_DIR, filename)

        if not os.path.exists(dest_path):
            print(f"📥 Downloading: {game_name}")
            download_image(img_url, dest_path)
        else:
            print(f"🖼 Already cached: {filename}")

if __name__ == "__main__":
    cache_images()
