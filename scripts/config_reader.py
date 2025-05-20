
import json
import os

def load_launcher_config(config_path="launcher_config.json"):
    if not os.path.exists(config_path):
        print(f"Launcher config not found at {config_path}")
        return {}

    with open(config_path, "r") as f:
        config = json.load(f)

    return config

def print_launcher_settings(config):
    print("=== Launcher Settings ===")
    for key, value in config.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    config = load_launcher_config()
    if config:
        print_launcher_settings(config)
