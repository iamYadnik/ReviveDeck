import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt
from scripts.steam_metadata_fetcher import fetch_all_metadata

class SteamMetadataViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steam Game Metadata Viewer")
        self.setGeometry(300, 200, 700, 500)
        self.games = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("🎮 Steam Games Metadata")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.refresh_button = QPushButton("🔄 Refresh Metadata")
        self.refresh_button.clicked.connect(self.load_metadata)
        layout.addWidget(self.refresh_button)

        self.setLayout(layout)
        self.load_metadata()

    def load_metadata(self):
        self.list_widget.clear()
        self.games = fetch_all_metadata()
        if not self.games:
            QMessageBox.warning(self, "No Metadata", "⚠️ No game metadata found.")
            return
        for game in self.games:
            name = game.get("name", "Unknown")
            appid = game.get("appid", "???")
            folder = game.get("install_path", "")
            item_text = f"{name} [AppID: {appid}] — Folder: {folder}"
            self.list_widget.addItem(item_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = SteamMetadataViewer()
    viewer.show()
    sys.exit(app.exec_())