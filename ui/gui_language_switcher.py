import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QComboBox, QPushButton, QMessageBox
)

CONFIG_PATH = "config/user_settings.json"
TRANSLATION_PATH = "config/translation_config.json"

class LanguageSwitcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Language Preferences")
        self.setGeometry(300, 250, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("🌍 Select your language:")
        layout.addWidget(self.label)

        self.dropdown = QComboBox()
        self.languages = self.load_supported_languages()
        self.dropdown.addItems(self.languages)
        layout.addWidget(self.dropdown)

        save_btn = QPushButton("Save Language")
        save_btn.clicked.connect(self.save_language)
        layout.addWidget(save_btn)

        self.setLayout(layout)
        self.load_current_language()

    def load_supported_languages(self):
        if os.path.exists(TRANSLATION_PATH):
            with open(TRANSLATION_PATH, "r") as f:
                data = json.load(f)
                return data.get("supported_languages", ["en"])
        return ["en"]

    def load_current_language(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                config = json.load(f)
                lang = config.get("language", "en")
                index = self.dropdown.findText(lang)
                if index >= 0:
                    self.dropdown.setCurrentIndex(index)

    def save_language(self):
        selected = self.dropdown.currentText()
        config = {}
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                config = json.load(f)
        config["language"] = selected
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=4)
        QMessageBox.information(self, "Saved", f"✅ Language set to {selected}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LanguageSwitcher()
    window.show()
    sys.exit(app.exec_())