import importlib
import os
import sys

PLUGINS_FOLDER = "plugins"

def load_plugins():
    if not os.path.exists(PLUGINS_FOLDER):
        print(f"⚠️ Plugin folder '{PLUGINS_FOLDER}' not found. Skipping plugin load.")
        return

    sys.path.insert(0, PLUGINS_FOLDER)
    for filename in os.listdir(PLUGINS_FOLDER):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, "register"):
                    module.register()
                    print(f"✅ Loaded plugin: {module_name}")
                else:
                    print(f"⚠️ Plugin '{module_name}' has no 'register()' method.")
            except Exception as e:
                print(f"❌ Failed to load plugin '{module_name}': {e}")
    sys.path.pop(0)

if __name__ == "__main__":
    print("🔌 Loading ReviveDeck plugins...")
    load_plugins()