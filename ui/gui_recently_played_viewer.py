import sys
import os
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt
from scripts.recently_played_tracker import get_recently_played
import subprocess

class RecentlyPlayedViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recently Played Games")
        self.setGeometry(300, 200, 700, 500)
        self.recents = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("🕹 Recently Played")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        self.launch_btn = QPushButton("🚀 Launch Selected")
        self.launch_btn.clicked.connect(self.launch_selected)
        layout.addWidget(self.launch_btn)

        self.setLayout(layout)
        self.load_recently_played()

    def load_recently_played(self):
        self.recents = get_recently_played()
        self.list_widget.clear()

        if not self.recents:
            self.list_widget.addItem("📭 No games played yet.")
            self.launch_btn.setEnabled(False)
            return

        for item in self.recents:
            name = item["game"]
            time = item["timestamp"]
            path = item.get("path", "N/A")
            self.list_widget.addItem(f"{name} — {time} — {path}")

        self.launch_btn.setEnabled(True)

    def launch_selected(self):
        item = self.list_widget.currentItem()
        if item:
            text = item.text()
            path = text.split("—")[-1].strip()
            if os.path.exists(path):
                try:
                    subprocess.Popen([path])
                    QMessageBox.information(self, "Launched", f"✅ Game launched:
{path}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"❌ Failed to launch:
{e}")
            else:
                QMessageBox.warning(self, "Not Found", "⚠️ Path does not exist or is invalid.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = RecentlyPlayedViewer()
    viewer.show()
    sys.exit(app.exec_())