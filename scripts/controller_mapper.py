import evdev
from evdev import InputDevice, categorize, ecodes, list_devices
import json
import os

MAPPING_FILE = "config/controller_mappings.json"

def detect_controllers():
    devices = [InputDevice(path) for path in list_devices()]
    gamepads = [d for d in devices if "event" in d.path and d.capabilities().get(ecodes.EV_ABS)]
    return gamepads

def map_controller_events(device_path):
    print(f"🎮 Listening for input from: {device_path}")
    dev = InputDevice(device_path)

    mappings = {}

    print("🔧 Press each button or move stick in the order prompted.")
    keys_to_map = ["A", "B", "X", "Y", "Start", "Select", "L1", "R1", "Up", "Down", "Left", "Right"]

    for label in keys_to_map:
        print(f"➡️ Press button for: {label}")
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
                key = ecodes.bytype[event.type][event.code]
                mappings[label] = key
                print(f"✅ Mapped {label} to {key}")
                break

    os.makedirs("config", exist_ok=True)
    with open(MAPPING_FILE, "w") as f:
        json.dump(mappings, f, indent=4)

    print(f"✅ Mappings saved to {MAPPING_FILE}")

if __name__ == "__main__":
    gamepads = detect_controllers()
    if not gamepads:
        print("❌ No compatible gamepads found.")
    else:
        print("🎮 Detected controllers:")
        for i, d in enumerate(gamepads):
            print(f"{i + 1}. {d.name} - {d.path}")
        choice = int(input("Select a controller to map (1-N): ")) - 1
        if 0 <= choice < len(gamepads):
            map_controller_events(gamepads[choice].path)