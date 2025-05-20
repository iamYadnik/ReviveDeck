import os
import json

FAV_PATH = "config/favorite_games.json"

def load_favorites():
    if os.path.exists(FAV_PATH):
        with open(FAV_PATH, "r") as f:
            return json.load(f)
    return []

def save_favorites(game_paths):
    os.makedirs("config", exist_ok=True)
    with open(FAV_PATH, "w") as f:
        json.dump(game_paths, f, indent=4)
    print(f"✅ Saved {len(game_paths)} favorites.")

def add_favorite(path):
    favorites = load_favorites()
    if path not in favorites:
        favorites.append(path)
        save_favorites(favorites)

def remove_favorite(path):
    favorites = load_favorites()
    if path in favorites:
        favorites.remove(path)
        save_favorites(favorites)

# Example usage
if __name__ == "__main__":
    test_game = "/home/user/.steam/steamapps/common/ExampleGame"
    add_favorite(test_game)
    print("⭐ Favorites:", load_favorites())