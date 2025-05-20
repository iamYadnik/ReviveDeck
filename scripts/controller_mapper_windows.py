import pygame
import json
import os
from time import sleep

CONFIG_PATH = "config/controller_windows_mappings.json"

def map_windows_controller():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("❌ No controller detected.")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"🎮 Detected: {joystick.get_name()}")

    os.makedirs("config", exist_ok=True)
    mapping = {}
    buttons = ["A", "B", "X", "Y", "L1", "R1", "Start", "Select", "Up", "Down", "Left", "Right"]

    print("🔧 Press each button or direction when prompted...")

    for label in buttons:
        print(f"➡️  Press: {label}")
        mapped = False
        while not mapped:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    mapping[label] = f"button_{event.button}"
                    mapped = True
                    print(f"✅ {label} -> button_{event.button}")
                elif event.type == pygame.JOYHATMOTION:
                    mapping[label] = f"hat_{event.value}"
                    mapped = True
                    print(f"✅ {label} -> hat_{event.value}")
            sleep(0.1)

    with open(CONFIG_PATH, "w") as f:
        json.dump(mapping, f, indent=4)
    print(f"✅ Mapping saved to {CONFIG_PATH}")

if __name__ == "__main__":
    map_windows_controller()