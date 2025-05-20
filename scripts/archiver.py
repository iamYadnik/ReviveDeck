
import os
import shutil
from datetime import datetime

ARCHIVE_DIR = "archive"
TARGETS = ["revivedeck.log", "launcher_config.json", "diagnostic_report.md"]

def archive_file(filename):
    if not os.path.exists(filename):
        print(f"⚠️ {filename} not found. Skipping.")
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    base_name = os.path.basename(filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archived_name = f"{base_name}.{timestamp}.bak"
    archived_path = os.path.join(ARCHIVE_DIR, archived_name)

    shutil.copy2(filename, archived_path)
    print(f"✅ Archived {filename} → {archived_path}")

if __name__ == "__main__":
    print("📦 Archiving important config and log files...")
    for file in TARGETS:
        archive_file(file)
    print("🏁 Archiving complete.")
