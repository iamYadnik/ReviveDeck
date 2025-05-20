
import subprocess
from datetime import datetime

def run_task(label, command):
    print(f"⏳ Running: {label}")
    try:
        subprocess.run(command, check=True)
        print(f"✅ Completed: {label}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed: {label}")

def schedule_tasks():
    print(f"🗓️ ReviveDeck Scheduled Task Run — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Define tasks as (description, command list)
    tasks = [
        ("Run Diagnostics", ["python3", "scripts/system_diagnostics.py"]),
        ("Archive Configs and Logs", ["python3", "scripts/archiver.py"]),
        ("Check for Updates", ["python3", "scripts/self_updater.py"]),
        ("Run File Integrity Check", ["python3", "scripts/file_integrity_checker.py"])
    ]

    for label, cmd in tasks:
        run_task(label, cmd)

    print("🎯 All scheduled tasks completed.")

if __name__ == "__main__":
    schedule_tasks()
