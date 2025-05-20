
import os
import subprocess
import sys
from time import sleep

REPO_DIR = os.path.abspath(".")
LAUNCH_COMMAND = ["python3", "ui/unified_gui_launcher.py"]

def update_repo():
    print("🔄 Checking for updates...")
    subprocess.run(["git", "-C", REPO_DIR, "pull"])

def restart_launcher():
    print("🚀 Restarting ReviveDeck...")
    sleep(1)
    subprocess.Popen(LAUNCH_COMMAND)
    sys.exit()

if __name__ == "__main__":
    update_repo()
    restart_launcher()
