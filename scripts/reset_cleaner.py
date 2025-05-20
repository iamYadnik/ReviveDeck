
import os
import shutil

FILES_TO_DELETE = [
    "revivedeck.log",
    "revivedeck_stats.json",
    "launcher_config.json",
    "diagnostic_report.md",
    "steam_games_metadata.json",
    "revivedeck_settings_export.zip"
]

FOLDERS_TO_DELETE = [
    "game_profiles",
    "test_configs",
    "users",
    "cache",
    "ReviveDeck.AppDir",
    "backups"
]

def confirm(prompt):
    response = input(f"{prompt} (y/N): ").strip().lower()
    return response == "y"

def reset_environment():
    print("⚠️ This will permanently delete all logs, configs, user data, and local assets.")
    if not confirm("Are you sure you want to proceed?"):
        print("❌ Cancelled.")
        return

    for file in FILES_TO_DELETE:
        if os.path.exists(file):
            os.remove(file)
            print(f"🗑️ Deleted file: {file}")

    for folder in FOLDERS_TO_DELETE:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"🧹 Removed folder: {folder}")

    print("✅ ReviveDeck environment has been reset.")

if __name__ == "__main__":
    reset_environment()
