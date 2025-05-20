import os
import zipfile
from datetime import datetime

INCLUDE = [
    "revivedeck.py",
    "ui/",
    "scripts/",
    "config/",
    "assets/",
    "logs/",
    "build_linux_installer.sh",
    "build_macos_app.sh",
    "build_windows_spec.py"
]

def zip_folder(zipf, folder, base):
    for root, _, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base)
            zipf.write(full_path, rel_path)

def create_zip():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    zip_name = f"ReviveDeck_{timestamp}.zip"
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for path in INCLUDE:
            if os.path.exists(path):
                if os.path.isdir(path):
                    zip_folder(zipf, path, ".")
                else:
                    zipf.write(path, os.path.relpath(path, "."))
    print(f"✅ Archive created: {zip_name}")

if __name__ == "__main__":
    create_zip()