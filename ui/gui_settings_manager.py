import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox, QMessageBox
)
from config.theme_engine import load_theme_config, apply_theme

CONFIG_PATH = "config/user_settings.json"

class SettingsManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Settings Manager")
        self.setGeometry(300, 300, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("🛠 Select your preferred theme:")
        layout.addWidget(self.label)

        self.dropdown = QComboBox()
        self.dropdown.addItems(["dark", "light"])
        layout.addWidget(self.dropdown)

        self.save_button = QPushButton("Save Settings")
        self.save_button.clicked.connect(self.save_settings)
        layout.addWidget(self.save_button)

        self.setLayout(layout)
        self.load_user_settings()

    def load_user_settings(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                settings = json.load(f)
                theme = settings.get("theme", "dark")
                self.dropdown.setCurrentText(theme)

    def save_settings(self):
        selected_theme = self.dropdown.currentText()
        with open(CONFIG_PATH, "w") as f:
            json.dump({"theme": selected_theme}, f, indent=4)
        QMessageBox.information(self, "Saved", "✅ Settings saved successfully!")
        apply_theme(QApplication.instance(), load_theme_config(), mode=selected_theme)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = load_theme_config()
    apply_theme(app, config)
    win = SettingsManager()
    win.show()
    sys.exit(app.exec_())