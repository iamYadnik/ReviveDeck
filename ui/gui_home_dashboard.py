
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
)
from PyQt5.QtGui import QPixmap
import subprocess
import os

class HomeDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Dashboard")
        self.setGeometry(250, 200, 600, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Add logo
        logo_path = "assets/revivedeck_splash.png"
        if os.path.exists(logo_path):
            logo = QLabel()
            pixmap = QPixmap(logo_path).scaledToWidth(500)
            logo.setPixmap(pixmap)
            layout.addWidget(logo)

        # Section title
        layout.addWidget(QLabel("📦 Tools & Utilities"))

        # Buttons for tools
        tools = {
            "Launch Game Manager": "ui/unified_gui_launcher.py",
            "View Stats Dashboard": "ui/gui_stats_dashboard.py",
            "Profile Diff Viewer": "ui/gui_profile_diff_viewer.py",
            "Run Backup Manager": "scripts/backup_manager.py",
            "Settings Import/Export": "scripts/settings_import_export.py",
            "Steam Game Sync": "scripts/steam_api_integrator.py"
        }

        for name, script in tools.items():
            btn = QPushButton(name)
            btn.clicked.connect(lambda checked, s=script: self.run_script(s))
            layout.addWidget(btn)

        self.setLayout(layout)

    def run_script(self, script_path):
        if not os.path.exists(script_path):
            QMessageBox.warning(self, "File Not Found", f"Script not found: {script_path}")
            return
        try:
            subprocess.Popen(["python", script_path])
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = HomeDashboard()
    win.show()
    sys.exit(app.exec_())
