import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QMessageBox
)

CONFIG_PATH = "config/feature_toggles.json"

class FeatureToggleManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Feature Toggle Manager")
        self.setGeometry(300, 300, 400, 300)
        self.toggles = {}
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.checkboxes = {}

        self.load_config()

        for feature, enabled in self.toggles.items():
            cb = QCheckBox(feature)
            cb.setChecked(enabled)
            self.checkboxes[feature] = cb
            layout.addWidget(cb)

        save_btn = QPushButton("Save Changes")
        save_btn.clicked.connect(self.save_config)
        layout.addWidget(save_btn)

        self.setLayout(layout)

    def load_config(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                data = json.load(f)
                self.toggles = data.get("enabled_features", {})

    def save_config(self):
        updated = {k: cb.isChecked() for k, cb in self.checkboxes.items()}
        with open(CONFIG_PATH, "w") as f:
            json.dump({"enabled_features": updated}, f, indent=4)
        QMessageBox.information(self, "Saved", "✅ Feature toggles updated successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FeatureToggleManager()
    window.show()
    sys.exit(app.exec_())