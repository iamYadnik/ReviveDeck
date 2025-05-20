
import requests
import json

# Replace with your actual Steam API key
STEAM_API_KEY = "YOUR_STEAM_API_KEY"
STEAM_ID = "YOUR_STEAM_ID"  # 64-bit SteamID
API_URL = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
APP_DETAILS_URL = "https://store.steampowered.com/api/appdetails"

def fetch_owned_games(api_key, steam_id):
    params = {
        "key": api_key,
        "steamid": steam_id,
        "include_appinfo": True,
        "format": "json"
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json().get("response", {}).get("games", [])
    else:
        print(f"❌ Failed to fetch game list: {response.status_code}")
        return []

def fetch_game_details(appid):
    response = requests.get(APP_DETAILS_URL, params={"appids": appid})
    if response.status_code == 200:
        data = response.json().get(str(appid), {})
        return data.get("data", {}) if data.get("success") else {}
    return {}

def save_game_metadata(games, output_file="steam_games_metadata.json"):
    metadata = {}
    for game in games[:10]:  # Limit for demo purposes
        appid = game["appid"]
        name = game["name"]
        print(f"📥 Fetching metadata for {name} (AppID: {appid})...")
        details = fetch_game_details(appid)
        metadata[name] = {
            "appid": appid,
            "name": name,
            "type": details.get("type", ""),
            "genres": details.get("genres", []),
            "release_date": details.get("release_date", {}).get("date", ""),
            "platforms": details.get("platforms", {}),
            "header_image": details.get("header_image", "")
        }

    with open(output_file, "w") as f:
        json.dump(metadata, f, indent=4)
    print(f"✅ Metadata saved to {output_file}")

if __name__ == "__main__":
    if "YOUR_STEAM_API_KEY" in STEAM_API_KEY or "YOUR_STEAM_ID" in STEAM_ID:
        print("⚠️ Please update STEAM_API_KEY and STEAM_ID before running.")
    else:
        games = fetch_owned_games(STEAM_API_KEY, STEAM_ID)
        save_game_metadata(games)
