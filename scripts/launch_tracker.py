import os
import json
from datetime import datetime

LOG_PATH = "logs/launch_counts.json"

def track_launch(tool_name):
    os.makedirs("logs", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")

    log_data = {}
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            try:
                log_data = json.load(f)
            except:
                log_data = {}

    if today not in log_data:
        log_data[today] = {}

    log_data[today][tool_name] = log_data[today].get(tool_name, 0) + 1

    with open(LOG_PATH, "w") as f:
        json.dump(log_data, f, indent=4)

    print(f"📈 Tracked: {tool_name} launched on {today}")

# Example
if __name__ == "__main__":
    track_launch("dashboard")