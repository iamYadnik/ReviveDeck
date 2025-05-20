import os
import subprocess
import platform
import json

LOG_PATH = "logs/game_launch_log.txt"

def run_game(executable_path, args=None):
    if not os.path.exists(executable_path):
        log_result(f"❌ Executable not found: {executable_path}")
        return False

    full_cmd = [executable_path] + (args if args else [])
    try:
        subprocess.Popen(full_cmd)
        log_result(f"✅ Launched: {' '.join(full_cmd)}")
        return True
    except Exception as e:
        log_result(f"❌ Failed to launch game: {e}")
        return False

def log_result(message):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(message + "\n")
    print(message)

# Example standalone usage
if __name__ == "__main__":
    game_path = input("Enter full path to game executable: ").strip()
    run_game(game_path)