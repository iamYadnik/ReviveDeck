import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PyQt5.QtGui import QFont
from config.theme_engine import load_theme_config, apply_theme

class ModuleBoilerplate(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Module")
        self.setGeometry(400, 300, 500, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title = QLabel("🔧 ReviveDeck Module Template")
        self.title.setFont(QFont("Arial", 16))
        layout.addWidget(self.title)

        self.label = QLabel("Start building your GUI module here.")
        layout.addWidget(self.label)

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def button_clicked(self):
        self.label.setText("🟢 Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = load_theme_config()
    apply_theme(app, config)
    window = ModuleBoilerplate()
    window.show()
    sys.exit(app.exec_())