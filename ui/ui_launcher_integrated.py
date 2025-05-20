
import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QPushButton, QListWidget, QMessageBox
)
from config_reader import load_launcher_config
from logger import log_launch, log_error


class ReviveDeckLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck - Game Launcher")
        self.setGeometry(100, 100, 600, 400)
        self.config = load_launcher_config()
        self.games = []
        self.setup_ui()
        self.load_games()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Installed Steam Games:")
        layout.addWidget(self.label)

        self.game_list = QListWidget()
        layout.addWidget(self.game_list)

        self.launch_button = QPushButton("Launch Game")
        self.launch_button.clicked.connect(self.launch_game)
        layout.addWidget(self.launch_button)

        self.setLayout(layout)

    def load_games(self):
        path = self.config.get("game_install_path", "")
        if not os.path.exists(path):
            log_error(f"Game install path not found: {path}")
            return
        self.games = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        self.game_list.addItems(self.games)

    def launch_game(self):
        selected = self.game_list.currentItem()
        if selected:
            game_name = selected.text()
            log_launch(game_name)
            QMessageBox.information(self, "Launching", f"Launching {game_name}...")
        else:
            QMessageBox.warning(self, "No Selection", "Please select a game first.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReviveDeckLauncher()
    window.show()
    sys.exit(app.exec_())
