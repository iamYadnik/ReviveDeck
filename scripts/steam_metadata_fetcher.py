import os
import re

def parse_appmanifest(manifest_path):
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            content = f.read()

        def extract(key):
            match = re.search(rf'\"{key}\"\s+\"(.+?)\"', content)
            return match.group(1) if match else None

        return {
            "appid": extract("appid"),
            "name": extract("name"),
            "size": extract("SizeOnDisk"),
            "install_path": extract("installdir")
        }
    except Exception as e:
        print(f"❌ Failed to parse {manifest_path}: {e}")
        return None

def fetch_all_metadata():
    steam_paths = [
        os.path.expanduser("~/.local/share/Steam/steamapps"),
        os.path.expanduser("~/.steam/steam/steamapps")
    ]
    results = []

    for steam_path in steam_paths:
        if not os.path.exists(steam_path):
            continue

        for file in os.listdir(steam_path):
            if file.startswith("appmanifest") and file.endswith(".acf"):
                metadata = parse_appmanifest(os.path.join(steam_path, file))
                if metadata:
                    metadata["manifest_file"] = file
                    results.append(metadata)

    return results

if __name__ == "__main__":
    games = fetch_all_metadata()
    for g in games:
        print(f"🎮 {g['name']} (AppID: {g['appid']}) — {g['install_path']}")