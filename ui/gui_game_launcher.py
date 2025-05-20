import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QLineEdit, QMessageBox
)
from scripts.game_runner import run_game

class GameLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Game Launcher")
        self.setGeometry(300, 300, 600, 200)
        self.executable_path = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("🎮 Select a game executable to launch:")
        layout.addWidget(self.label)

        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Game executable path...")
        layout.addWidget(self.path_input)

        browse_btn = QPushButton("📂 Browse")
        browse_btn.clicked.connect(self.browse_file)
        layout.addWidget(browse_btn)

        launch_btn = QPushButton("🚀 Launch Game")
        launch_btn.clicked.connect(self.launch_game)
        layout.addWidget(launch_btn)

        self.setLayout(layout)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Game Executable")
        if file_path:
            self.executable_path = file_path
            self.path_input.setText(file_path)

    def launch_game(self):
        path = self.path_input.text().strip()
        if path:
            success = run_game(path)
            if success:
                QMessageBox.information(self, "Game Launched", f"✅ Game launched:
{path}")
            else:
                QMessageBox.critical(self, "Launch Failed", "❌ Failed to launch game.")
        else:
            QMessageBox.warning(self, "No Path", "⚠️ Please select a game executable.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = GameLauncher()
    launcher.show()
    sys.exit(app.exec_())