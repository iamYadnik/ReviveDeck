import os
import json
import subprocess

SETTINGS_PATH = "config/user_settings.json"

def check_first_run():
    if not os.path.exists(SETTINGS_PATH):
        return True
    try:
        with open(SETTINGS_PATH, "r") as f:
            settings = json.load(f)
            return not settings.get("welcome_shown", False)
    except:
        return True

def mark_welcome_shown():
    settings = {}
    if os.path.exists(SETTINGS_PATH):
        try:
            with open(SETTINGS_PATH, "r") as f:
                settings = json.load(f)
        except:
            settings = {}
    settings["welcome_shown"] = True
    os.makedirs("config", exist_ok=True)
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=4)

def run_welcome_if_first():
    if check_first_run():
        print("🎉 First run detected. Launching welcome screen...")
        subprocess.run(["python", "ui/gui_welcome_screen.py"])
        mark_welcome_shown()
    else:
        print("✅ Welcome screen already shown. Skipping.")

if __name__ == "__main__":
    run_welcome_if_first()