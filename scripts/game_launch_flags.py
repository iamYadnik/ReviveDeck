import os
import json

FLAGS_FILE = "config/launch_flags.json"

def load_flags():
    if os.path.exists(FLAGS_FILE):
        with open(FLAGS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_flags(flags):
    os.makedirs("config", exist_ok=True)
    with open(FLAGS_FILE, "w") as f:
        json.dump(flags, f, indent=4)
    print("✅ Launch flags saved.")

def set_launch_flag(app_id, arguments):
    flags = load_flags()
    flags[app_id] = arguments
    save_flags(flags)

def get_launch_flag(app_id):
    return load_flags().get(app_id, [])

# Example usage
if __name__ == "__main__":
    print("1. Set launch flags")
    print("2. View all launch flags")
    choice = input("Choose (1-2): ").strip()

    if choice == "1":
        app_id = input("Enter Steam AppID or unique game ID: ").strip()
        args = input("Enter launch arguments (space-separated): ").strip().split()
        set_launch_flag(app_id, args)
    elif choice == "2":
        for k, v in load_flags().items():
            print(f"🛠 {k}: {' '.join(v)}")