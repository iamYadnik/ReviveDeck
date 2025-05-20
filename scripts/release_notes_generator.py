import re
import os

CHANGELOG_PATH = "CHANGELOG.md"
OUTPUT_PATH = "docs/generated_release_notes.md"

def extract_latest_release():
    if not os.path.exists(CHANGELOG_PATH):
        print("❌ CHANGELOG.md not found.")
        return

    with open(CHANGELOG_PATH, "r") as f:
        lines = f.readlines()

    release_notes = []
    capture = False

    for line in lines:
        if line.startswith("## ") and not capture:
            capture = True
            release_notes.append(line)
            continue
        elif line.startswith("## ") and capture:
            break
        elif capture:
            release_notes.append(line)

    with open(OUTPUT_PATH, "w") as out:
        out.writelines(release_notes)

    print(f"✅ Release notes generated at {OUTPUT_PATH}")

if __name__ == "__main__":
    extract_latest_release()