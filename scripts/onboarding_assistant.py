
import os
import json
import shutil

WELCOME = """
🎮 Welcome to ReviveDeck!
--------------------------
Let's get you set up with your first configuration.

This onboarding assistant will help you:
- Create your first user profile
- Configure launcher settings
- Run setup scripts
"""

DEFAULT_USER = "player1"
DEFAULT_CONFIG = {
    "preferred_resolution": "1280x720",
    "fps_cap": 30,
    "vsync": False,
    "language": "en",
    "theme": "dark",
    "auto_optimize": True,
    "game_install_path": "/home/user/.steam/steam/steamapps/common/",
    "mode": "gamer"
}

def create_user_profile(username):
    os.makedirs("users", exist_ok=True)
    profile_path = os.path.join("users", f"{username}.json")
    if not os.path.exists(profile_path):
        with open(profile_path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        print(f"✅ Created profile: {profile_path}")
    else:
        print(f"⚠️ Profile already exists: {profile_path}")
    return profile_path

def initialize_main_config(profile_path):
    with open(profile_path, "r") as f:
        user_config = json.load(f)
    with open("launcher_config.json", "w") as f:
        json.dump(user_config, f, indent=4)
    print("✅ Initialized launcher_config.json with default user profile.")

def run_setup():
    if os.path.exists("setup.sh"):
        print("📦 Running setup script...")
        os.system("chmod +x setup.sh && ./setup.sh")
    else:
        print("⚠️ setup.sh not found. Skipping...")

def main():
    print(WELCOME)
    username = input("Enter your desired username (default: player1): ").strip() or DEFAULT_USER
    profile_path = create_user_profile(username)
    initialize_main_config(profile_path)
    run_setup()
    print("\n🎉 Onboarding complete! Launch the GUI with:")
    print("python ui/unified_gui_launcher.py")

if __name__ == "__main__":
    main()
