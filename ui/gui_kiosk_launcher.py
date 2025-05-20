import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PyQt5.QtCore import Qt
import subprocess

class KioskLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Kiosk Mode")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        title = QLabel("🎮 ReviveDeck - Kiosk Mode")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold;")

        layout.addWidget(title)

        buttons = {
            "Launch Dashboard": "ui/gui_home_dashboard.py",
            "System Info": "ui/gui_system_info.py",
            "Stats Viewer": "ui/gui_stats_dashboard.py",
            "Exit Kiosk Mode": "exit"
        }

        for label, command in buttons.items():
            btn = QPushButton(label)
            btn.setFixedHeight(60)
            btn.setStyleSheet("font-size: 18px;")
            if command == "exit":
                btn.clicked.connect(self.close)
            else:
                btn.clicked.connect(lambda _, cmd=command: subprocess.Popen(["python", cmd]))
            layout.addWidget(btn)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = KioskLauncher()
    win.show()
    sys.exit(app.exec_())