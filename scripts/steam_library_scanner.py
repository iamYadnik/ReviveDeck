import os
import re

def find_steam_libraries():
    # Default Steam path by OS
    if os.name == "nt":
        steam_path = os.path.join(os.environ['ProgramFiles(x86)'], "Steam", "steamapps")
    elif os.name == "posix":
        steam_path = os.path.expanduser("~/.steam/steam/steamapps")
        if not os.path.exists(steam_path):
            steam_path = os.path.expanduser("~/.local/share/Steam/steamapps")
    else:
        return []

    libraries = [steam_path]
    library_vdf = os.path.join(steam_path, "libraryfolders.vdf")

    if not os.path.exists(library_vdf):
        print("⚠️ Steam libraryfolders.vdf not found.")
        return libraries

    try:
        with open(library_vdf, "r", encoding="utf-8") as f:
            content = f.read()

        found = re.findall(r'\t"\d+"\t"(.+?)"', content)
        for path in found:
            game_path = os.path.join(path.replace("\\", "\"), "steamapps")
            if os.path.exists(game_path) and game_path not in libraries:
                libraries.append(game_path)
    except Exception as e:
        print(f"❌ Failed to parse libraryfolders.vdf: {e}")

    return libraries

def find_installed_games():
    libraries = find_steam_libraries()
    game_dirs = []

    for lib in libraries:
        common_path = os.path.join(lib, "common")
        if os.path.exists(common_path):
            for game in os.listdir(common_path):
                full_path = os.path.join(common_path, game)
                if os.path.isdir(full_path):
                    game_dirs.append(full_path)
    return game_dirs

# Example usage
if __name__ == "__main__":
    games = find_installed_games()
    for g in games:
        print("🎮", g)