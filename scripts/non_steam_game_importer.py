import os
import json
from tkinter import Tk, filedialog

NON_STEAM_CONFIG = "config/non_steam_games.json"

def load_non_steam():
    if os.path.exists(NON_STEAM_CONFIG):
        with open(NON_STEAM_CONFIG, "r") as f:
            return json.load(f)
    return []

def save_non_steam(games):
    os.makedirs("config", exist_ok=True)
    with open(NON_STEAM_CONFIG, "w") as f:
        json.dump(games, f, indent=4)
    print("✅ Non-Steam games saved.")

def import_non_steam_game():
    Tk().withdraw()
    path = filedialog.askopenfilename(title="Select Game Executable")
    if not path:
        print("❌ No file selected.")
        return

    name = input("Enter game name to display: ").strip()
    game = {"name": name, "path": path}
    games = load_non_steam()
    games.append(game)
    save_non_steam(games)

def list_non_steam_games():
    games = load_non_steam()
    if not games:
        print("📭 No non-Steam games added.")
    else:
        for g in games:
            print(f"🎮 {g['name']} — {g['path']}")

if __name__ == "__main__":
    print("1. Import a non-Steam game")
    print("2. View imported games")
    choice = input("Choose (1-2): ").strip()

    if choice == "1":
        import_non_steam_game()
    elif choice == "2":
        list_non_steam_games()