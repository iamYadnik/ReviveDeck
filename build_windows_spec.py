# build_windows_spec.py — creates a bundled .exe for ReviveDeck on Windows

import os
import subprocess

def build_exe():
    if not os.path.exists("revivedeck.py"):
        print("❌ Error: revivedeck.py not found in root directory.")
        return

    print("📦 Building Windows executable using PyInstaller...")
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "ReviveDeck",
        "--icon", "assets/revivedeck_icon.ico",
        "revivedeck.py"
    ])
    print("✅ Build complete. Check the /dist folder.")

if __name__ == "__main__":
    build_exe()