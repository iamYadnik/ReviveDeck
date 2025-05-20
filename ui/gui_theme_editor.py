import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QColorDialog

CONFIG_PATH = "config/theme_config.json"

class ThemeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Theme Editor - ReviveDeck")
        self.setGeometry(300, 300, 500, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.fields = {
            "background": QLineEdit(),
            "foreground": QLineEdit(),
            "button": QLineEdit(),
            "highlight": QLineEdit()
        }

        for key, input_box in self.fields.items():
            input_box.setPlaceholderText(f"{key} color hex (e.g. #ffffff)")
            layout.addWidget(QLabel(f"{key.capitalize()} Color:"))
            layout.addWidget(input_box)
            btn = QPushButton(f"Pick {key}")
            btn.clicked.connect(lambda _, k=key: self.pick_color(k))
            layout.addWidget(btn)

        self.save_button = QPushButton("Save Custom Theme")
        self.save_button.clicked.connect(self.save_theme)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def pick_color(self, key):
        color = QColorDialog.getColor()
        if color.isValid():
            self.fields[key].setText(color.name())

    def save_theme(self):
        try:
            theme = {
                "custom": {k: self.fields[k].text().strip() for k in self.fields},
                "theme": "custom"
            }
            with open(CONFIG_PATH, "w") as f:
                json.dump(theme, f, indent=4)
            QMessageBox.information(self, "Success", "✅ Custom theme saved!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"❌ Failed to save theme: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ThemeEditor()
    editor.show()
    sys.exit(app.exec_())