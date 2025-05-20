import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea,
    QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from scripts.steam_metadata_fetcher import fetch_all_metadata
from scripts.game_runner import run_game

class GameCard(QWidget):
    def __init__(self, name, appid, install_path):
        super().__init__()
        self.name = name
        self.install_path = install_path
        self.setStyleSheet("QFrame { border: 1px solid #ccc; padding: 10px; }")
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        img = QLabel()
        pixmap = QPixmap("assets/placeholder_icon.png").scaled(64, 64, Qt.KeepAspectRatio)
        img.setPixmap(pixmap)
        layout.addWidget(img)

        info_layout = QVBoxLayout()
        info_layout.addWidget(QLabel(f"<b>{self.name}</b>"))
        info_layout.addWidget(QLabel(f"AppID: {appid}"))
        layout.addLayout(info_layout)

        launch_btn = QPushButton("🚀 Launch")
        launch_btn.clicked.connect(self.launch_game)
        layout.addWidget(launch_btn)

        self.setLayout(layout)

    def launch_game(self):
        # Try launching the first .exe, .sh, or .AppImage in install path
        for file in os.listdir(self.install_path):
            if file.endswith(('.exe', '.sh', '.AppImage')):
                full_path = os.path.join(self.install_path, file)
                run_game(full_path)
                break

class GameCardLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Card Launcher")
        self.setGeometry(300, 150, 800, 600)
        self.init_ui()

    def init_ui(self):
        scroll = QScrollArea()
        container = QWidget()
        vbox = QVBoxLayout(container)

        games = fetch_all_metadata()
        for game in games:
            card = QFrame()
            layout = QVBoxLayout(card)
            widget = GameCard(game["name"], game["appid"], os.path.join(
                os.path.expanduser("~/.local/share/Steam/steamapps/common/"),
                game["install_path"]
            ))
            layout.addWidget(widget)
            vbox.addWidget(card)

        scroll.setWidgetResizable(True)
        scroll.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GameCardLauncher()
    win.show()
    sys.exit(app.exec_())