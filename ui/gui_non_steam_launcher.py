import sys
import os
import json
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton,
    QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import Qt

NON_STEAM_CONFIG = "config/non_steam_games.json"

def load_non_steam():
    if os.path.exists(NON_STEAM_CONFIG):
        with open(NON_STEAM_CONFIG, "r") as f:
            return json.load(f)
    return []

def save_non_steam(games):
    os.makedirs("config", exist_ok=True)
    with open(NON_STEAM_CONFIG, "w") as f:
        json.dump(games, f, indent=4)

class NonSteamLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎮 Non-Steam Games")
        self.setGeometry(300, 200, 700, 500)
        self.games = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("📂 Imported Non-Steam Games"))

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        btn_row = QHBoxLayout()
        self.launch_btn = QPushButton("🚀 Launch")
        self.remove_btn = QPushButton("🗑 Remove")
        btn_row.addWidget(self.launch_btn)
        btn_row.addWidget(self.remove_btn)
        layout.addLayout(btn_row)

        self.setLayout(layout)
        self.launch_btn.clicked.connect(self.launch_game)
        self.remove_btn.clicked.connect(self.remove_game)

        self.load_games()

    def load_games(self):
        self.games = load_non_steam()
        self.list_widget.clear()
        if not self.games:
            self.list_widget.addItem("📭 No non-Steam games added.")
            self.launch_btn.setEnabled(False)
            self.remove_btn.setEnabled(False)
        else:
            for game in self.games:
                self.list_widget.addItem(f"{game['name']} — {game['path']}")
            self.launch_btn.setEnabled(True)
            self.remove_btn.setEnabled(True)

    def launch_game(self):
        selected = self.list_widget.currentRow()
        if selected >= 0 and selected < len(self.games):
            path = self.games[selected]["path"]
            if os.path.exists(path):
                subprocess.Popen([path])
                QMessageBox.information(self, "Launching", f"✅ Game launched:
{path}")
            else:
                QMessageBox.warning(self, "Not Found", "⚠️ File not found.")

    def remove_game(self):
        selected = self.list_widget.currentRow()
        if selected >= 0 and selected < len(self.games):
            confirm = QMessageBox.question(self, "Confirm", "Remove this game from the list?", QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.games.pop(selected)
                save_non_steam(self.games)
                self.load_games()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NonSteamLauncher()
    win.show()
    sys.exit(app.exec_())