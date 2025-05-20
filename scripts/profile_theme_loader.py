import os
import json
from config.theme_engine import load_theme_config, apply_theme

CURRENT_PROFILE_PATH = "config/current_profile.json"
PROFILES_DIR = "config/profiles/"

def load_profile_theme(app):
    # Step 1: Find active profile
    if not os.path.exists(CURRENT_PROFILE_PATH):
        print("⚠️ No current_profile.json found.")
        return

    with open(CURRENT_PROFILE_PATH, "r") as f:
        current = json.load(f).get("active_profile", "")

    profile_path = os.path.join(PROFILES_DIR, f"{current}.json")
    if not os.path.exists(profile_path):
        print(f"❌ Profile not found: {profile_path}")
        return

    # Step 2: Check for theme preference
    with open(profile_path, "r") as f:
        profile = json.load(f)
        theme = profile.get("preferred_theme")

    if not theme:
        print("🧾 No theme set in profile. Using default.")
        return

    # Step 3: Apply theme using your existing engine
    config = load_theme_config()
    apply_theme(app, config, mode=theme)
    print(f"✅ Loaded profile-specific theme: {theme}")

# Example usage inside any GUI launcher:
# from profile_theme_loader import load_profile_theme
# load_profile_theme(QApplication.instance())