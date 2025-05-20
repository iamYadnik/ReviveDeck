import json
import os

CURRENT_PROFILE_PATH = "config/current_profile.json"
PROFILES_DIR = "config/profiles/"

def load_last_profile():
    if not os.path.exists(CURRENT_PROFILE_PATH):
        print("⚠️ No current_profile.json file found.")
        return None
    try:
        with open(CURRENT_PROFILE_PATH, "r") as f:
            data = json.load(f)
            profile = data.get("active_profile")
            profile_path = os.path.join(PROFILES_DIR, f"{profile}.json")
            if os.path.exists(profile_path):
                print(f"✅ Loaded active profile: {profile}")
                return profile_path
            else:
                print(f"❌ Profile file not found: {profile_path}")
                return None
    except Exception as e:
        print(f"❌ Failed to load profile: {e}")
        return None

if __name__ == "__main__":
    load_last_profile()