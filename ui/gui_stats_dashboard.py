
import sys
import os
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QListWidget, QListWidgetItem, QMessageBox
)
from datetime import timedelta

STATS_FILE = "revivedeck_stats.json"

class StatsDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck - Usage Stats Dashboard")
        self.setGeometry(300, 300, 500, 400)
        self.setup_ui()
        self.load_stats()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.title = QLabel("📊 Game Usage Statistics")
        self.title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(self.title)

        self.stats_list = QListWidget()
        layout.addWidget(self.stats_list)

        self.setLayout(layout)

    def load_stats(self):
        if not os.path.exists(STATS_FILE):
            QMessageBox.warning(self, "Stats Not Found", f"No stats file found at {STATS_FILE}")
            return

        with open(STATS_FILE, "r") as f:
            stats = json.load(f)

        for game, data in stats.items():
            launches = data.get("launches", 0)
            last_played = data.get("last_played", "Never")
            total_seconds = data.get("total_time_seconds", 0)
            duration = str(timedelta(seconds=total_seconds))
            display = f"🎮 {game}\n - Launches: {launches}\n - Last Played: {last_played}\n - Time Played: {duration}"
            item = QListWidgetItem(display)
            self.stats_list.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StatsDashboard()
    window.show()
    sys.exit(app.exec_())
