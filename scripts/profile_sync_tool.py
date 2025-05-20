
import os
import shutil
import subprocess
from datetime import datetime

REMOTE_URL = "https://github.com/YOUR_USERNAME/revivedeck-profiles.git"
LOCAL_DIR = "synced_profiles"
PROFILE_DIR = "game_profiles"

def clone_remote_repo():
    if os.path.exists(LOCAL_DIR):
        print(f"📁 {LOCAL_DIR} already exists, skipping clone.")
    else:
        print("🔄 Cloning profile repository...")
        subprocess.run(["git", "clone", REMOTE_URL, LOCAL_DIR])

def sync_to_remote():
    print("📤 Syncing local profiles to remote...")
    clone_remote_repo()
    for filename in os.listdir(PROFILE_DIR):
        full_path = os.path.join(PROFILE_DIR, filename)
        if os.path.isfile(full_path):
            shutil.copy(full_path, os.path.join(LOCAL_DIR, filename))

    os.chdir(LOCAL_DIR)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Update profiles - {datetime.now().isoformat()}"])
    subprocess.run(["git", "push"])
    os.chdir("..")
    print("✅ Profiles pushed to remote.")

def sync_from_remote():
    print("📥 Syncing profiles from remote to local...")
    clone_remote_repo()
    for filename in os.listdir(LOCAL_DIR):
        src = os.path.join(LOCAL_DIR, filename)
        dest = os.path.join(PROFILE_DIR, filename)
        if os.path.isfile(src):
            shutil.copy(src, dest)
    print("✅ Profiles pulled and copied to game_profiles/.")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Sync TO remote")
    print("2. Sync FROM remote")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        sync_to_remote()
    elif choice == "2":
        sync_from_remote()
    else:
        print("❌ Invalid choice.")
