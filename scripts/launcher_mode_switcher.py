
import json
import os

CONFIG_PATH = "launcher_config.json"
VALID_MODES = ["gamer", "developer"]

def set_mode(mode):
    if mode not in VALID_MODES:
        print(f"❌ Invalid mode. Choose from: {', '.join(VALID_MODES)}")
        return

    if not os.path.exists(CONFIG_PATH):
        print(f"⚠️ Config file not found: {CONFIG_PATH}")
        return

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    config["mode"] = mode

    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

    print(f"✅ Launcher mode set to: {mode}")

def show_mode():
    if not os.path.exists(CONFIG_PATH):
        print(f"⚠️ Config file not found: {CONFIG_PATH}")
        return

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    mode = config.get("mode", "gamer")
    print(f"🔄 Current launcher mode: {mode}")

if __name__ == "__main__":
    print("Select mode:")
    print("1. Gamer Mode")
    print("2. Developer Mode")
    print("3. Show Current Mode")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        set_mode("gamer")
    elif choice == "2":
        set_mode("developer")
    elif choice == "3":
        show_mode()
    else:
        print("❌ Invalid selection.")
