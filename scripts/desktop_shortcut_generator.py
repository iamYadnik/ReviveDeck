
import os

DESKTOP_ENTRY = """[Desktop Entry]
Name=ReviveDeck Launcher
Comment=Unified game and config launcher for ReviveDeck
Exec=python3 {exec_path}
Icon=utilities-terminal
Terminal=false
Type=Application
Categories=Game;Utility;
"""

def create_shortcut():
    exec_path = os.path.abspath("ui/unified_gui_launcher.py")
    shortcut_content = DESKTOP_ENTRY.format(exec_path=exec_path)

    desktop_dir = os.path.expanduser("~/.local/share/applications")
    os.makedirs(desktop_dir, exist_ok=True)

    shortcut_path = os.path.join(desktop_dir, "revivedeck.desktop")
    with open(shortcut_path, "w") as f:
        f.write(shortcut_content)

    os.chmod(shortcut_path, 0o755)
    print(f"✅ Desktop shortcut created at: {shortcut_path}")

if __name__ == "__main__":
    create_shortcut()
