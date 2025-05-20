
import os
import shutil
import subprocess

APP_DIR = "ReviveDeck.AppDir"
BIN_DIR = os.path.join(APP_DIR, "usr", "bin")
DESKTOP_FILE = os.path.join(APP_DIR, "revivedeck.desktop")
ICON_FILE = os.path.join(APP_DIR, "revivedeck.png")
APPIMAGE_TOOL_URL = "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"

def setup_app_dir():
    os.makedirs(BIN_DIR, exist_ok=True)

    # Copy entry point
    shutil.copy("ui/unified_gui_launcher.py", os.path.join(BIN_DIR, "revivedeck"))

    # Create desktop entry
    with open(DESKTOP_FILE, "w") as f:
        f.write("""[Desktop Entry]
Name=ReviveDeck
Exec=revivedeck
Icon=revivedeck
Type=Application
Categories=Game;
""")

    # Generate a placeholder icon
    with open(ICON_FILE, "wb") as f:
        f.write(b"")  # You can replace with actual PNG bytes or skip

def bundle_appimage():
    print("📦 Bundling ReviveDeck AppImage...")
    if not os.path.exists("appimagetool.AppImage"):
        print("⬇️  Download appimagetool manually from:")
        print(APPIMAGE_TOOL_URL)
        return

    os.chmod("appimagetool.AppImage", 0o755)
    subprocess.run(["./appimagetool.AppImage", APP_DIR])
    print("✅ ReviveDeck.AppImage should now be built in the current directory.")

if __name__ == "__main__":
    setup_app_dir()
    bundle_appimage()
