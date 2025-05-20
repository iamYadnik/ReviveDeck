import os
import json
from datetime import datetime

LOG_PATH = "logs/recently_played.json"
os.makedirs("logs", exist_ok=True)

def log_game_launch(game_name, launch_path=None):
    entry = {
        "game": game_name,
        "timestamp": datetime.now().isoformat(),
        "path": launch_path
    }

    logs = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []

    logs.append(entry)
    logs = sorted(logs, key=lambda x: x["timestamp"], reverse=True)[:50]

    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"✅ Logged: {game_name}")

def get_recently_played():
    if not os.path.exists(LOG_PATH):
        return []
    with open(LOG_PATH, "r") as f:
        return json.load(f)

# Standalone usage for demo/view
if __name__ == "__main__":
    recents = get_recently_played()
    if not recents:
        print("📭 No games played yet.")
    else:
        print("🕹 Recently Played:")
        for item in recents:
            print(f" - {item['game']} @ {item['timestamp']}")