
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
)
import subprocess

class UnifiedLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Unified Launcher")
        self.setGeometry(200, 200, 400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Welcome to ReviveDeck Toolkit")
        layout.addWidget(label)

        btn1 = QPushButton("🛠 Launch Game Interface")
        btn1.clicked.connect(lambda: self.run_script("ui/ui_launcher_integrated.py"))
        layout.addWidget(btn1)

        btn2 = QPushButton("📓 View Logs")
        btn2.clicked.connect(lambda: self.run_script("ui/log_viewer_gui.py"))
        layout.addWidget(btn2)

        btn3 = QPushButton("⚙️ Edit Config")
        btn3.clicked.connect(lambda: self.run_script("ui/config_editor_gui.py"))
        layout.addWidget(btn3)

        btn4 = QPushButton("👤 Manage Users")
        btn4.clicked.connect(lambda: self.run_script("scripts/multi_user_manager.py", terminal=True))
        layout.addWidget(btn4)

        btn5 = QPushButton("🧪 Generate Diagnostics")
        btn5.clicked.connect(lambda: self.run_script("scripts/system_diagnostics.py", terminal=True))
        layout.addWidget(btn5)

        self.setLayout(layout)

    def run_script(self, path, terminal=False):
        try:
            if terminal:
                subprocess.Popen(["x-terminal-emulator", "-e", f"python3 {path}"])
            else:
                subprocess.Popen(["python3", path])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to launch {path}\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = UnifiedLauncher()
    launcher.show()
    sys.exit(app.exec_())
