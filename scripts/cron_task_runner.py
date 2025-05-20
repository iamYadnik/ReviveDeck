import time
import datetime
import subprocess

# Define your periodic tasks here (name, interval in seconds, command)
TASKS = [
    {
        "name": "Export Usage Stats",
        "interval": 3600,
        "command": ["python", "scripts/usage_stats_exporter.py"]
    },
    {
        "name": "Run Plugin Validator",
        "interval": 7200,
        "command": ["python", "plugin_validator.py"]
    }
]

def run_cron_tasks():
    print("⏳ ReviveDeck Cron Task Runner started...")
    last_run = {task['name']: 0 for task in TASKS}

    try:
        while True:
            now = time.time()
            for task in TASKS:
                if now - last_run[task["name"]] >= task["interval"]:
                    print(f"🔁 Running: {task['name']} @ {datetime.datetime.now().isoformat()}")
                    try:
                        subprocess.run(task["command"], check=True)
                    except subprocess.CalledProcessError as e:
                        print(f"❌ Task '{task['name']}' failed: {e}")
                    last_run[task["name"]] = now
            time.sleep(10)
    except KeyboardInterrupt:
        print("🛑 Cron runner terminated by user.")

if __name__ == "__main__":
    run_cron_tasks()