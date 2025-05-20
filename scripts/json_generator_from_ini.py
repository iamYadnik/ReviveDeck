
import os
import configparser
import json

def convert_ini_to_json(ini_path, game_name, output_dir="game_profiles"):
    if not os.path.exists(ini_path):
        print(f"INI file not found: {ini_path}")
        return

    config = configparser.ConfigParser()
    config.read(ini_path)

    profile = {
        "ini_overrides": {},
        "cfg_overrides": {}
    }

    for section in config.sections():
        profile["ini_overrides"][section] = {}
        for key, val in config.items(section):
            profile["ini_overrides"][section][key] = val

    os.makedirs(output_dir, exist_ok=True)
    json_path = os.path.join(output_dir, f"{game_name.lower().replace(' ', '_')}.json")
    with open(json_path, "w") as f:
        json.dump(profile, f, indent=4)

    print(f"JSON profile saved to {json_path}")

if __name__ == "__main__":
    # Example usage
    ini_file = "test_configs/sample_game.ini"
    convert_ini_to_json(ini_file, "sample_game")
