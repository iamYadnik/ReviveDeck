
import os
import zipfile

EXPORT_NAME = "revivedeck_settings_export.zip"
EXPORT_ITEMS = [
    "launcher_config.json",
    "revivedeck_stats.json",
    "revivedeck.log",
    "users/",
    "game_profiles/",
    "test_configs/"
]

def export_settings():
    with zipfile.ZipFile(EXPORT_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in EXPORT_ITEMS:
            if os.path.isdir(item):
                for root, _, files in os.walk(item):
                    for file in files:
                        path = os.path.join(root, file)
                        arcname = os.path.relpath(path)
                        zipf.write(path, arcname)
                        print(f"📁 Added: {arcname}")
            elif os.path.isfile(item):
                zipf.write(item)
                print(f"📄 Added: {item}")
            else:
                print(f"⚠️ Skipped (not found): {item}")
    print(f"✅ Settings exported to {EXPORT_NAME}")

def import_settings(zip_path):
    if not os.path.exists(zip_path):
        print(f"❌ Zip file not found: {zip_path}")
        return

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall()
        print(f"✅ Settings imported from {zip_path}")

if __name__ == "__main__":
    print("ReviveDeck Settings Sync")
    print("1. Export Settings")
    print("2. Import Settings")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        export_settings()
    elif choice == "2":
        zip_path = input("Enter path to import .zip: ").strip()
        import_settings(zip_path)
    else:
        print("❌ Invalid selection.")
