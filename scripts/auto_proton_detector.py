import os
import glob

def find_proton_installations():
    possible_paths = [
        "~/.steam/steam/steamapps/common",
        "~/.local/share/Steam/steamapps/common"
    ]
    detected = []

    for base in possible_paths:
        path = os.path.expanduser(base)
        if os.path.exists(path):
            for item in os.listdir(path):
                if "proton" in item.lower():
                    full_path = os.path.join(path, item)
                    if os.path.isdir(full_path):
                        detected.append(full_path)

    return detected

def get_latest_proton():
    installs = find_proton_installations()
    if not installs:
        print("❌ No Proton installations found.")
        return None

    # Sort versions numerically if possible
    installs.sort(reverse=True)
    print("✅ Proton installations found:")
    for p in installs:
        print(" -", p)
    return installs[0]  # Return latest

# Example usage
if __name__ == "__main__":
    latest = get_latest_proton()
    if latest:
        print(f"🧪 Auto-detected Proton: {latest}")