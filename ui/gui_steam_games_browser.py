import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt
from scripts.steam_library_scanner import find_installed_games
from scripts.game_runner import run_game
import os

class SteamGamesBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steam Games Browser")
        self.setGeometry(300, 200, 700, 500)
        self.games = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("🎮 Detected Steam Games")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.refresh_button = QPushButton("🔄 Refresh Game List")
        self.refresh_button.clicked.connect(self.load_games)
        layout.addWidget(self.refresh_button)

        self.launch_button = QPushButton("🚀 Launch Selected Game")
        self.launch_button.clicked.connect(self.launch_game)
        layout.addWidget(self.launch_button)

        self.setLayout(layout)
        self.load_games()

    def load_games(self):
        self.list_widget.clear()
        self.games = find_installed_games()
        for g in self.games:
            self.list_widget.addItem(g)

    def launch_game(self):
        selected = self.list_widget.currentItem()
        if selected:
            path = selected.text()
            # Attempt to find an executable in the folder
            exec_found = False
            for file in os.listdir(path):
                if file.endswith(('.exe', '.sh', '.AppImage')):
                    exec_path = os.path.join(path, file)
                    exec_found = True
                    success = run_game(exec_path)
                    if success:
                        QMessageBox.information(self, "Launched", f"✅ Launched: {exec_path}")
                    else:
                        QMessageBox.critical(self, "Failed", f"❌ Failed to launch: {exec_path}")
                    break
            if not exec_found:
                QMessageBox.warning(self, "Not Found", "⚠️ No executable found in selected folder.")
        else:
            QMessageBox.warning(self, "No Game", "⚠️ Please select a game from the list.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = SteamGamesBrowser()
    browser.show()
    sys.exit(app.exec_())