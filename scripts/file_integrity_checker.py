
import os
import json
import configparser

def validate_json(file_path):
    try:
        with open(file_path, "r") as f:
            json.load(f)
        return True
    except Exception as e:
        print(f"❌ Invalid JSON: {file_path}\n   → {e}")
        return False

def validate_ini(file_path):
    try:
        parser = configparser.ConfigParser()
        parser.read(file_path)
        return True
    except Exception as e:
        print(f"❌ Invalid INI: {file_path}\n   → {e}")
        return False

def run_integrity_check():
    passed = 0
    failed = 0

    print("🔍 Checking game_profiles/ for valid JSON...")
    for filename in os.listdir("game_profiles"):
        if filename.endswith(".json"):
            full_path = os.path.join("game_profiles", filename)
            if validate_json(full_path):
                print(f"✅ {filename}")
                passed += 1
            else:
                failed += 1

    print("\n🔍 Checking test_configs/ for valid INI files...")
    for filename in os.listdir("test_configs"):
        if filename.endswith(".ini"):
            full_path = os.path.join("test_configs", filename)
            if validate_ini(full_path):
                print(f"✅ {filename}")
                passed += 1
            else:
                failed += 1

    print(f"\n✅ Passed: {passed} file(s)")
    print(f"❌ Failed: {failed} file(s)")

if __name__ == "__main__":
    run_integrity_check()
