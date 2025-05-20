import os
import json
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QComboBox, QMessageBox
)

PROFILES_DIR = "config/profiles/"
CURRENT_PROFILE_PATH = "config/current_profile.json"

class ProfileSwitcher(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        self.label = QLabel("Active Profile:")
        self.dropdown = QComboBox()
        self.dropdown.currentIndexChanged.connect(self.set_active_profile)

        layout.addWidget(self.label)
        layout.addWidget(self.dropdown)
        self.setLayout(layout)

        self.load_profiles()

    def load_profiles(self):
        os.makedirs(PROFILES_DIR, exist_ok=True)
        self.dropdown.clear()
        profiles = [f[:-5] for f in os.listdir(PROFILES_DIR) if f.endswith(".json")]
        self.dropdown.addItems(profiles)
        self.load_current_profile()

    def load_current_profile(self):
        if os.path.exists(CURRENT_PROFILE_PATH):
            with open(CURRENT_PROFILE_PATH, "r") as f:
                current = json.load(f).get("active_profile", "")
                index = self.dropdown.findText(current)
                if index >= 0:
                    self.dropdown.setCurrentIndex(index)

    def set_active_profile(self):
        selected = self.dropdown.currentText()
        with open(CURRENT_PROFILE_PATH, "w") as f:
            json.dump({"active_profile": selected}, f, indent=4)
        QMessageBox.information(self, "Profile Switched", f"✅ Active profile: {selected}")