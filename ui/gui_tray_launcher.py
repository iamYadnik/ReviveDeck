import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import subprocess
import os

class TrayLauncher:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)

        icon_path = "assets/revivedeck_icon.png"
        self.tray = QSystemTrayIcon(QIcon(icon_path), self.app)
        self.menu = QMenu()

        tools = {
            "Dashboard": "ui/gui_home_dashboard.py",
            "Settings": "ui/gui_settings_manager.py",
            "System Info": "ui/gui_system_info.py",
            "Backup & Restore": "ui/gui_backup_restore.py",
            "Stats Dashboard": "ui/gui_stats_dashboard.py"
        }

        for name, path in tools.items():
            action = QAction(name)
            action.triggered.connect(lambda checked, p=path: self.launch_tool(p))
            self.menu.addAction(action)

        self.menu.addSeparator()
        quit_action = QAction("Exit")
        quit_action.triggered.connect(self.exit_app)
        self.menu.addAction(quit_action)

        self.tray.setContextMenu(self.menu)
        self.tray.setToolTip("ReviveDeck Launcher")
        self.tray.show()

    def launch_tool(self, path):
        subprocess.Popen(["python", path])

    def exit_app(self):
        self.tray.hide()
        self.app.quit()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    launcher = TrayLauncher()
    launcher.run()