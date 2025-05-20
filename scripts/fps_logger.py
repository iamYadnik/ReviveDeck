import subprocess
import time
import os
import json
from datetime import datetime

LOG_PATH = "logs/performance_log.json"
os.makedirs("logs", exist_ok=True)

def log_performance(game_name, duration=10):
    # Simulated FPS sample generator (replace with real metric when integrated)
    fps_data = []
    print(f"📊 Simulating FPS logging for: {game_name} (Duration: {duration}s)")

    for second in range(duration):
        fps = 50 + (second % 10)  # Fake fluctuation between 50–59 FPS
        fps_data.append({"second": second + 1, "fps": fps})
        time.sleep(1)

    log_entry = {
        "game": game_name,
        "timestamp": datetime.now().isoformat(),
        "duration_sec": duration,
        "fps_samples": fps_data
    }

    logs = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []

    logs.append(log_entry)

    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"✅ FPS log saved to {LOG_PATH}")
    return log_entry

if __name__ == "__main__":
    name = input("Enter game name: ").strip()
    duration = input("Log duration in seconds (default 10): ").strip()
    duration = int(duration) if duration.isdigit() else 10
    log_performance(name, duration)