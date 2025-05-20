
import os
import subprocess
import json

CONFIG_PATH = "launcher_config.json"
STEAM_COMPAT_TOOL_PATH = os.path.expanduser("~/.steam/steam/steamapps/common/Proton 8.0/proton")

def get_game_path(game_name):
    config = {}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)

    base_path = config.get("game_install_path", "")
    game_path = os.path.join(base_path, game_name)
    if not os.path.exists(game_path):
        print(f"❌ Game directory not found: {game_path}")
        return None

    # Look for .exe file
    for root, _, files in os.walk(game_path):
        for file in files:
            if file.endswith(".exe"):
                return os.path.join(root, file)

    print("❌ No .exe file found in game directory.")
    return None

def launch_game_with_proton(game_name):
    exe_path = get_game_path(game_name)
    if not exe_path:
        return

    print(f"🚀 Launching {game_name} with Proton...")
    command = [STEAM_COMPAT_TOOL_PATH, "run", exe_path]
    try:
        subprocess.run(command)
    except Exception as e:
        print(f"❌ Failed to launch game: {e}")

if __name__ == "__main__":
    game = input("Enter the name of the game folder to launch: ").strip()
    launch_game_with_proton(game)
