
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar, QGraphicsOpacityEffect
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class SplashLoader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Launching ReviveDeck...")
        self.setFixedSize(600, 400)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: #1e1e1e;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Add splash image if available
        pixmap = QPixmap("assets/revivedeck_splash.png")
        if not pixmap.isNull():
            splash = QLabel()
            splash.setPixmap(pixmap.scaledToWidth(500, Qt.SmoothTransformation))
            splash.setAlignment(Qt.AlignCenter)
            layout.addWidget(splash)

        # Add loading text and progress bar
        self.status = QLabel("Loading...")
        self.status.setStyleSheet("color: white; font-size: 18px;")
        self.status.setAlignment(Qt.AlignCenter)

        self.progress = QProgressBar()
        self.progress.setStyleSheet(
            "QProgressBar { background-color: #444; color: white; border: 1px solid #555; height: 20px; }"
            "QProgressBar::chunk { background-color: #ff9800; width: 20px; }"
        )
        self.progress.setValue(0)

        layout.addWidget(self.status)
        layout.addWidget(self.progress)

        self.setLayout(layout)
        self.load_simulation()

    def load_simulation(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.advance)
        self.progress_value = 0
        self.timer.start(50)

    def advance(self):
        if self.progress_value >= 100:
            self.timer.stop()
            self.close()  # In production, trigger main launcher here
        else:
            self.progress_value += 2
            self.progress.setValue(self.progress_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashLoader()
    splash.show()
    sys.exit(app.exec_())
