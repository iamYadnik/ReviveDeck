import os
import json
from datetime import datetime

LOG_PATH = "logs/feedback_log.json"

def log_feedback(text, checklist=None):
    os.makedirs("logs", exist_ok=True)
    entry = {
        "timestamp": datetime.now().isoformat(),
        "feedback": text.strip(),
        "completed": checklist or []
    }

    data = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    data.append(entry)

    with open(LOG_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Feedback saved to logs/feedback_log.json")

# Example usage
if __name__ == "__main__":
    log_feedback("I love this app!", ["theme", "dashboard"])