import os
import subprocess
from pathlib import Path

# Adjust this to your installed Proton path or fetch dynamically later
DEFAULT_PROTON_PATH = os.path.expanduser("~/.steam/steam/steamapps/common/Proton 8.0/proton")

def run_with_proton(exe_path, proton_path=DEFAULT_PROTON_PATH, args=None):
    if not os.path.exists(exe_path):
        print(f"❌ Game not found: {exe_path}")
        return False

    if not os.path.exists(proton_path):
        print(f"❌ Proton not found at: {proton_path}")
        return False

    # Set up required env
    steam_compat = {
        "STEAM_COMPAT_CLIENT_INSTALL_PATH": os.path.expanduser("~/.steam/steam"),
        "STEAM_COMPAT_DATA_PATH": os.path.expanduser(f"~/.steam/steam/steamapps/compatdata/{hash(exe_path) % 999999}/")
    }

    command = [proton_path, "run", exe_path] + (args or [])
    try:
        subprocess.Popen(command, env={**os.environ, **steam_compat})
        print(f"🚀 Running with Proton: {' '.join(command)}")
        return True
    except Exception as e:
        print(f"❌ Failed to run with Proton: {e}")
        return False

# Example usage
if __name__ == "__main__":
    path = input("Enter path to .exe file: ").strip()
    run_with_proton(path)