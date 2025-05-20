
import os
from datetime import datetime

LOG_FILE = "revivedeck.log"

def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{level}] {message}\n"
    with open(LOG_FILE, "a") as f:
        f.write(line)

def log_launch(game_name):
    log(f"Game launched: {game_name}")

def log_error(error_message):
    log(f"ERROR: {error_message}", level="ERROR")

def log_system_info(info: dict):
    log("System Info:")
    for key, value in info.items():
        log(f"  {key}: {value}")

if __name__ == "__main__":
    log("Logger initialized.")
    log_launch("Witcher 3")
    log_error("Test error message.")
