
import os
import json
import configparser

# This script modifies .ini or .cfg files in the game's config directory to apply low-spec performance tweaks.

def apply_game_optimizations(game_name, config_file_path, profile_dir="game_profiles"):
    profile_path = os.path.join(profile_dir, f"{game_name.lower().replace(' ', '_')}.json")
    if not os.path.exists(profile_path):
        print(f"No optimization profile found for {game_name}.")
        return

    with open(profile_path, 'r') as f:
        profile = json.load(f)

    if config_file_path.endswith(".ini"):
        parser = configparser.ConfigParser()
        parser.read(config_file_path)

        for section, options in profile.get("ini_overrides", {}).items():
            if not parser.has_section(section):
                parser.add_section(section)
            for key, value in options.items():
                parser.set(section, key, str(value))

        with open(config_file_path, 'w') as configfile:
            parser.write(configfile)
        print(f"Optimizations applied to {config_file_path}")

    elif config_file_path.endswith(".cfg"):
        # Simple line-by-line replacement
        with open(config_file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            key = line.split('=')[0].strip()
            value = profile.get("cfg_overrides", {}).get(key)
            if value is not None:
                new_lines.append(f"{key}={value}\n")
            else:
                new_lines.append(line)

        with open(config_file_path, 'w') as file:
            file.writelines(new_lines)
        print(f"Optimizations applied to {config_file_path}")
    else:
        print("Unsupported config file format.")

if __name__ == "__main__":
    # Example test call
    apply_game_optimizations("witcher3", "/home/user/.local/share/The Witcher 3/user.settings")
