import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton,
    QLabel, QMessageBox, QFileDialog, QHBoxLayout
)
from scripts.favorites_manager import load_favorites, add_favorite, remove_favorite, save_favorites
from scripts.game_runner import run_game

class FavoriteGamesLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Favorite Games Launcher")
        self.setGeometry(300, 200, 700, 500)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("⭐ Favorite Games"))

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.refresh_button = QPushButton("🔄 Refresh List")
        self.refresh_button.clicked.connect(self.load_favorites)
        layout.addWidget(self.refresh_button)

        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton("➕ Add Game")
        self.add_button.clicked.connect(self.add_game)
        buttons_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("➖ Remove Selected")
        self.remove_button.clicked.connect(self.remove_game)
        buttons_layout.addWidget(self.remove_button)

        self.launch_button = QPushButton("🚀 Launch Selected")
        self.launch_button.clicked.connect(self.launch_game)
        buttons_layout.addWidget(self.launch_button)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)
        self.load_favorites()

    def load_favorites(self):
        self.list_widget.clear()
        self.favorites = load_favorites()
        for path in self.favorites:
            self.list_widget.addItem(path)

    def add_game(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Game Executable")
        if file_path:
            add_favorite(file_path)
            self.load_favorites()

    def remove_game(self):
        selected = self.list_widget.currentItem()
        if selected:
            remove_favorite(selected.text())
            self.load_favorites()

    def launch_game(self):
        selected = self.list_widget.currentItem()
        if selected:
            success = run_game(selected.text())
            if success:
                QMessageBox.information(self, "Launched", f"✅ Game launched:
{selected.text()}")
            else:
                QMessageBox.critical(self, "Failed", "❌ Failed to launch selected game.")
        else:
            QMessageBox.warning(self, "No Selection", "⚠️ Please select a game to launch.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FavoriteGamesLauncher()
    window.show()
    sys.exit(app.exec_())