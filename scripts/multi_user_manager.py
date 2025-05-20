
import os
import json

USERS_DIR = "users"
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
    os.makedirs(USERS_DIR, exist_ok=True)
    profile_path = os.path.join(USERS_DIR, f"{username}.json")
    if os.path.exists(profile_path):
        print(f"⚠️ User '{username}' already exists.")
    else:
        with open(profile_path, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        print(f"✅ Created profile for user: {username}")

def switch_user(username):
    profile_path = os.path.join(USERS_DIR, f"{username}.json")
    if not os.path.exists(profile_path):
        print(f"❌ No profile found for '{username}'.")
        return

    with open(profile_path, "r") as src, open("launcher_config.json", "w") as dest:
        dest.write(src.read())
    print(f"🔄 Switched to user profile: {username}")

def list_users():
    if not os.path.exists(USERS_DIR):
        print("No user profiles found.")
        return
    print("👥 Available user profiles:")
    for file in os.listdir(USERS_DIR):
        if file.endswith(".json"):
            print(f" - {file.replace('.json', '')}")

if __name__ == "__main__":
    print("1. Create New User")
    print("2. Switch User")
    print("3. List Users")
    choice = input("Select an option (1/2/3): ").strip()

    if choice == "1":
        username = input("Enter new username: ").strip()
        create_user_profile(username)
    elif choice == "2":
        username = input("Enter username to switch to: ").strip()
        switch_user(username)
    elif choice == "3":
        list_users()
    else:
        print("❌ Invalid choice.")
