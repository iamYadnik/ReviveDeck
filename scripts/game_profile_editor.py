
import json
import os

def create_profile():
    game_name = input("Enter the game name: ").strip()
    profile = {
        "ini_overrides": {},
        "cfg_overrides": {}
    }

    print("\nAdd INI overrides (e.g. resolution, VSync):")
    while True:
        section = input("INI Section (leave empty to stop): ").strip()
        if not section:
            break
        if section not in profile["ini_overrides"]:
            profile["ini_overrides"][section] = {}
        while True:
            key = input(f"  Key for section [{section}] (empty to stop): ").strip()
            if not key:
                break
            value = input(f"  Value for '{key}': ").strip()
            profile["ini_overrides"][section][key] = value

    print("\nAdd CFG overrides (e.g. maxfps, shadows):")
    while True:
        key = input("CFG Key (leave empty to stop): ").strip()
        if not key:
            break
        value = input(f"  Value for '{key}': ").strip()
        profile["cfg_overrides"][key] = value

    profile_dir = "game_profiles"
    os.makedirs(profile_dir, exist_ok=True)
    file_name = os.path.join(profile_dir, f"{game_name.lower().replace(' ', '_')}.json")
    with open(file_name, 'w') as f:
        json.dump(profile, f, indent=4)

    print(f"\nProfile saved to {file_name}")

if __name__ == "__main__":
    create_profile()
