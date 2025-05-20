
import json
import os
from difflib import unified_diff

def load_json(path):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return None
    with open(path, "r") as f:
        return json.load(f)

def compare_profiles(file1, file2):
    print(f"🔍 Comparing profiles:\n- {file1}\n- {file2}\n")

    profile1 = load_json(file1)
    profile2 = load_json(file2)

    if profile1 is None or profile2 is None:
        return

    # Serialize JSON for line-by-line comparison
    json1 = json.dumps(profile1, indent=4).splitlines(keepends=True)
    json2 = json.dumps(profile2, indent=4).splitlines(keepends=True)

    diff = unified_diff(
        json1, json2,
        fromfile=os.path.basename(file1),
        tofile=os.path.basename(file2),
        lineterm=""
    )

    diff_output = list(diff)
    if diff_output:
        print("🧾 Differences found:")
        for line in diff_output:
            print(line)
    else:
        print("✅ Profiles are identical.")

if __name__ == "__main__":
    file1 = input("Enter path to first JSON profile: ").strip()
    file2 = input("Enter path to second JSON profile: ").strip()
    compare_profiles(file1, file2)
