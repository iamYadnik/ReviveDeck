import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt
import subprocess

class ReviveDeckLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Launcher")
        self.setGeometry(300, 200, 600, 400)
        self.init_ui()

    def init_ui(self):
        central = QWidget()
        layout = QVBoxLayout()

        title = QPushButton("🎮 Open Game Dashboard")
        title.setFixedHeight(60)
        title.clicked.connect(lambda: self.launch_ui("ui/gui_home_dashboard.py"))
        layout.addWidget(title)

        fav = QPushButton("⭐ Open Favorites")
        fav.setFixedHeight(50)
        fav.clicked.connect(lambda: self.launch_ui("ui/gui_favorite_games_launcher.py"))
        layout.addWidget(fav)

        steam = QPushButton("🧩 Browse Steam Games")
        steam.setFixedHeight(50)
        steam.clicked.connect(lambda: self.launch_ui("ui/gui_steam_games_browser.py"))
        layout.addWidget(steam)

        recent = QPushButton("🔁 Recently Played")
        recent.setFixedHeight(50)
        recent.clicked.connect(lambda: self.launch_ui("ui/gui_recently_played_viewer.py"))
        layout.addWidget(recent)

        search = QPushButton("🔍 Search Games")
        search.setFixedHeight(50)
        search.clicked.connect(lambda: self.launch_ui("ui/gui_game_search.py"))
        layout.addWidget(search)

        kiosk = QPushButton("🖥 Kiosk Mode")
        kiosk.setFixedHeight(50)
        kiosk.clicked.connect(lambda: self.launch_ui("ui/gui_kiosk_launcher.py"))
        layout.addWidget(kiosk)

        central.setLayout(layout)
        self.setCentralWidget(central)

    def launch_ui(self, script_path):
        try:
            subprocess.Popen(["python", script_path])
        except Exception as e:
            print(f"❌ Error launching {script_path}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = ReviveDeckLauncher()
    launcher.show()
    sys.exit(app.exec_())