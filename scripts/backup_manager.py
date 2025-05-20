
import os
import zipfile
from datetime import datetime

BACKUP_FOLDER = "backups"
FILES_TO_BACKUP = [
    "launcher_config.json",
    "revivedeck.log",
    "diagnostic_report.md"
]
FOLDERS_TO_BACKUP = [
    "game_profiles",
    "test_configs",
    "users"
]

def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(BACKUP_FOLDER, exist_ok=True)
    backup_file = os.path.join(BACKUP_FOLDER, f"revivedeck_backup_{timestamp}.zip")

    with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in FILES_TO_BACKUP:
            if os.path.exists(file):
                zipf.write(file)
                print(f"📁 Added file: {file}")
        for folder in FOLDERS_TO_BACKUP:
            for root, _, files in os.walk(folder):
                for name in files:
                    full_path = os.path.join(root, name)
                    arcname = os.path.relpath(full_path)
                    zipf.write(full_path, arcname)
                    print(f"📁 Added from folder: {arcname}")
    print(f"✅ Backup created: {backup_file}")

def restore_backup(zip_path):
    if not os.path.exists(zip_path):
        print("❌ Backup file does not exist.")
        return
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall()
        print(f"✅ Backup restored from: {zip_path}")

if __name__ == "__main__":
    print("ReviveDeck Backup Manager")
    print("1. Create Backup")
    print("2. Restore Backup")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        create_backup()
    elif choice == "2":
        zip_path = input("Enter path to backup .zip file: ").strip()
        restore_backup(zip_path)
    else:
        print("❌ Invalid selection.")
