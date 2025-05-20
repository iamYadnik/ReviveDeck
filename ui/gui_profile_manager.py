import os
import json
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QLineEdit, QMessageBox
)

PROFILES_DIR = "config/profiles"

class ProfileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Profile Manager")
        self.setGeometry(350, 200, 500, 400)
        self.init_ui()

    def init_ui(self):
        os.makedirs(PROFILES_DIR, exist_ok=True)

        layout = QVBoxLayout()

        self.label = QLabel("🧑‍💻 User Profiles")
        layout.addWidget(self.label)

        self.profile_list = QListWidget()
        layout.addWidget(self.profile_list)

        input_layout = QHBoxLayout()
        self.new_profile_input = QLineEdit()
        self.new_profile_input.setPlaceholderText("Enter new profile name")
        self.add_button = QPushButton("Add Profile")
        self.add_button.clicked.connect(self.add_profile)
        input_layout.addWidget(self.new_profile_input)
        input_layout.addWidget(self.add_button)
        layout.addLayout(input_layout)

        self.delete_button = QPushButton("Delete Selected Profile")
        self.delete_button.clicked.connect(self.delete_profile)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)
        self.load_profiles()

    def load_profiles(self):
        self.profile_list.clear()
        profiles = os.listdir(PROFILES_DIR)
        for profile in profiles:
            if profile.endswith(".json"):
                self.profile_list.addItem(profile[:-5])

    def add_profile(self):
        name = self.new_profile_input.text().strip()
        if not name:
            return
        profile_path = os.path.join(PROFILES_DIR, f"{name}.json")
        if os.path.exists(profile_path):
            QMessageBox.warning(self, "Error", "Profile already exists.")
            return
        with open(profile_path, "w") as f:
            json.dump({"profile_name": name}, f, indent=4)
        self.new_profile_input.clear()
        self.load_profiles()

    def delete_profile(self):
        selected = self.profile_list.currentItem()
        if selected:
            name = selected.text()
            profile_path = os.path.join(PROFILES_DIR, f"{name}.json")
            os.remove(profile_path)
            self.load_profiles()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ProfileManager()
    win.show()
    sys.exit(app.exec_())