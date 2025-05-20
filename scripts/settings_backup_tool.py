import os
import shutil
import datetime
import json
from pathlib import Path

BACKUP_DIR = "backups"
CONFIG_DIR = "config"
FILES_TO_BACKUP = ["user_settings.json", "theme_config.json", "favorite_games.json"]

def create_local_backup():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(backup_path, exist_ok=True)

    for file in FILES_TO_BACKUP:
        src = os.path.join(CONFIG_DIR, file)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(backup_path, file))

    print(f"✅ Local backup created at {backup_path}")
    return backup_path

def list_backups():
    if not os.path.exists(BACKUP_DIR):
        return []
    return sorted(os.listdir(BACKUP_DIR), reverse=True)

def restore_backup(backup_name):
    path = os.path.join(BACKUP_DIR, backup_name)
    if not os.path.isdir(path):
        print(f"❌ Backup not found: {backup_name}")
        return False

    for file in FILES_TO_BACKUP:
        src = os.path.join(path, file)
        dest = os.path.join(CONFIG_DIR, file)
        if os.path.exists(src):
            shutil.copy(src, dest)

    print(f"✅ Restored backup from {backup_name}")
    return True

if __name__ == "__main__":
    print("1. Create Backup")
    print("2. List Backups")
    print("3. Restore Backup")
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        create_local_backup()
    elif choice == "2":
        for b in list_backups():
            print("📁", b)
    elif choice == "3":
        backups = list_backups()
        for i, b in enumerate(backups):
            print(f"{i+1}. {b}")
        idx = int(input("Select backup to restore: ")) - 1
        if 0 <= idx < len(backups):
            restore_backup(backups[idx])
        else:
            print("❌ Invalid choice.")