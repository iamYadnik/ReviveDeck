
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget, QMessageBox

class ReviveDeckLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck - Steam Game Launcher")
        self.setGeometry(100, 100, 600, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Installed Steam Games:")
        layout.addWidget(self.label)

        self.game_list = QListWidget()
        self.game_list.addItem("Witcher 3")
        self.game_list.addItem("Assassin's Creed II")
        self.game_list.addItem("Skyrim")
        layout.addWidget(self.game_list)

        self.launch_button = QPushButton("Launch Game")
        self.launch_button.clicked.connect(self.launch_game)
        layout.addWidget(self.launch_button)

        self.setLayout(layout)

    def launch_game(self):
        selected_game = self.game_list.currentItem()
        if selected_game:
            QMessageBox.information(self, "Launching", f"Launching {selected_game.text()}...")
            # Here you would connect to the real launcher backend
        else:
            QMessageBox.warning(self, "No Game Selected", "Please select a game to launch.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReviveDeckLauncher()
    window.show()
    sys.exit(app.exec_())
