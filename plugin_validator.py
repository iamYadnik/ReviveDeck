import os
import importlib.util

PLUGINS_FOLDER = "plugins"

def is_valid_plugin(path):
    spec = importlib.util.spec_from_file_location("plugin", path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            return hasattr(module, "register")
        except Exception as e:
            print(f"❌ Error loading {path}: {e}")
            return False
    return False

def validate_plugins():
    if not os.path.exists(PLUGINS_FOLDER):
        print(f"📁 Plugin folder '{PLUGINS_FOLDER}' does not exist.")
        return

    print("🔍 Validating plugins...")
    for filename in os.listdir(PLUGINS_FOLDER):
        if filename.endswith(".py") and not filename.startswith("__"):
            filepath = os.path.join(PLUGINS_FOLDER, filename)
            valid = is_valid_plugin(filepath)
            if valid:
                print(f"✅ Valid plugin: {filename}")
            else:
                print(f"⚠️ Invalid or broken plugin: {filename}")

if __name__ == "__main__":
    validate_plugins()