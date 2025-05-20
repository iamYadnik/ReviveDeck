
import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QMessageBox, QCheckBox
)

CONFIG_PATH = "launcher_config.json"

class ConfigEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Config Editor")
        self.setGeometry(200, 200, 500, 350)
        self.setup_ui()
        self.load_config()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.fields = {}

        field_defs = [
            ("preferred_resolution", "Resolution (e.g. 1280x720)"),
            ("fps_cap", "FPS Cap"),
            ("vsync", "Enable VSync", "checkbox"),
            ("language", "Language (e.g. en)"),
            ("theme", "Theme (dark/light)"),
            ("auto_optimize", "Auto Optimize", "checkbox"),
            ("game_install_path", "Game Install Path")
        ]

        for key, label, *type_hint in field_defs:
            row = QHBoxLayout()
            lbl = QLabel(label)
            row.addWidget(lbl)

            if type_hint and type_hint[0] == "checkbox":
                widget = QCheckBox()
            else:
                widget = QLineEdit()

            row.addWidget(widget)
            layout.addLayout(row)
            self.fields[key] = widget

        self.save_button = QPushButton("Save Config")
        self.save_button.clicked.connect(self.save_config)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def load_config(self):
        if not os.path.exists(CONFIG_PATH):
            QMessageBox.warning(self, "Missing Config", f"{CONFIG_PATH} not found.")
            return
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        for key, widget in self.fields.items():
            if isinstance(widget, QCheckBox):
                widget.setChecked(bool(config.get(key, False)))
            else:
                widget.setText(str(config.get(key, "")))

    def save_config(self):
        config = {}
        for key, widget in self.fields.items():
            if isinstance(widget, QCheckBox):
                config[key] = widget.isChecked()
            else:
                config[key] = widget.text()
        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=4)
        QMessageBox.information(self, "Saved", "Configuration saved successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ConfigEditor()
    editor.show()
    sys.exit(app.exec_())
