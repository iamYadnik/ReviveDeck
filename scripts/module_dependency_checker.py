import os
import importlib.util
import traceback

SEARCH_PATHS = ["plugins", "scripts", "ui"]

def check_imports(path):
    failures = []
    for filename in os.listdir(path):
        if filename.endswith(".py") and not filename.startswith("__"):
            file_path = os.path.join(path, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
            try:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                print(f"✅ {filename} imported successfully.")
            except Exception as e:
                print(f"❌ {filename} failed to import:")
                traceback.print_exc()
                failures.append(filename)
    return failures

def run_dependency_check():
    print("🔎 Checking module imports...
")
    all_failures = []
    for folder in SEARCH_PATHS:
        if not os.path.exists(folder):
            continue
        print(f"📁 Scanning {folder}/")
        failures = check_imports(folder)
        if failures:
            all_failures.extend([f"{folder}/{f}" for f in failures])
    if not all_failures:
        print("\n🎉 All modules imported successfully!")
    else:
        print("\n⚠️ The following modules failed to import:")
        for fail in all_failures:
            print(f" - {fail}")

if __name__ == "__main__":
    run_dependency_check()