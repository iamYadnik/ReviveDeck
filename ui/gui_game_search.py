import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget,
    QLabel, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt
from scripts.steam_library_scanner import find_installed_games

class GameSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Search & Filter")
        self.setGeometry(300, 250, 700, 500)
        self.games = []
        self.filtered_games = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("🔍 Search for a game by title")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Type to filter games...")
        self.search_bar.textChanged.connect(self.filter_games)
        layout.addWidget(self.search_bar)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.launch_button = QPushButton("🚀 Launch Selected Game")
        self.launch_button.clicked.connect(self.launch_game)
        layout.addWidget(self.launch_button)

        self.setLayout(layout)
        self.load_games()

    def load_games(self):
        self.games = find_installed_games()
        self.filtered_games = self.games.copy()
        self.update_list()

    def filter_games(self, text):
        self.filtered_games = [g for g in self.games if text.lower() in g.lower()]
        self.update_list()

    def update_list(self):
        self.list_widget.clear()
        for g in self.filtered_games:
            self.list_widget.addItem(g)

    def launch_game(self):
        selected = self.list_widget.currentItem()
        if selected:
            import subprocess
            import os
            path = selected.text()
            for file in os.listdir(path):
                if file.endswith(('.exe', '.sh', '.AppImage')):
                    full_path = os.path.join(path, file)
                    subprocess.Popen([full_path])
                    QMessageBox.information(self, "Launching", f"✅ Launching:
{full_path}")
                    return
            QMessageBox.warning(self, "Not Found", "⚠️ No executable found in selected folder.")
        else:
            QMessageBox.warning(self, "No Selection", "⚠️ Please select a game to launch.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameSearch()
    window.show()
    sys.exit(app.exec_())