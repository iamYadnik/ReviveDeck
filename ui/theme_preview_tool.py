import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QComboBox
)
from config.theme_engine import load_theme_config, apply_theme

class ThemePreviewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Theme Previewer")
        self.setGeometry(300, 300, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Select a theme to preview")
        layout.addWidget(label)

        self.dropdown = QComboBox()
        self.dropdown.addItems(["dark", "light"])
        layout.addWidget(self.dropdown)

        preview_btn = QPushButton("Apply Theme")
        preview_btn.clicked.connect(self.change_theme)
        layout.addWidget(preview_btn)

        self.status = QLabel("")
        layout.addWidget(self.status)

        self.setLayout(layout)

    def change_theme(self):
        theme_choice = self.dropdown.currentText()
        config = load_theme_config()
        apply_theme(QApplication.instance(), config, mode=theme_choice)
        self.status.setText(f"✅ {theme_choice.capitalize()} theme applied.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    preview = ThemePreviewer()
    config_path = "config/theme_config.json"
    if not os.path.exists(config_path):
        preview.status.setText("❌ Theme config file not found.")
    else:
        apply_theme(app, load_theme_config())
    preview.show()
    sys.exit(app.exec_())