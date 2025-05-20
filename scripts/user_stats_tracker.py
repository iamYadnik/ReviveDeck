
import os
import json
import time
from datetime import datetime

STATS_FILE = "revivedeck_stats.json"

def log_game_launch(game_name):
    stats = {}
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            stats = json.load(f)

    if game_name not in stats:
        stats[game_name] = {
            "launches": 0,
            "last_played": "",
            "total_time_seconds": 0
        }

    stats[game_name]["launches"] += 1
    stats[game_name]["last_played"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)

    print(f"🎮 Logged launch: {game_name}")

def track_game_session(game_name):
    print(f"▶️ Starting session for: {game_name}")
    start = time.time()
    input("⏹ Press Enter when you finish playing...")
    end = time.time()

    duration = int(end - start)

    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            stats = json.load(f)
    else:
        stats = {}

    if game_name not in stats:
        stats[game_name] = {
            "launches": 1,
            "last_played": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_time_seconds": 0
        }

    stats[game_name]["total_time_seconds"] += duration
    stats[game_name]["last_played"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)

    print(f"✅ Session saved: {game_name} ({duration} seconds)")

if __name__ == "__main__":
    print("1. Log Game Launch")
    print("2. Track Game Session")
    choice = input("Choose (1/2): ").strip()
    game = input("Enter game name: ").strip()

    if choice == "1":
        log_game_launch(game)
    elif choice == "2":
        track_game_session(game)
    else:
        print("❌ Invalid choice.")
