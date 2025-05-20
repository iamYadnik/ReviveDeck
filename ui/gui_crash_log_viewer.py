import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog
)

DEFAULT_LOG_PATH = "logs/error_log.txt"

class CrashLogViewer(QWidget):
    def __init__(self, log_path=DEFAULT_LOG_PATH):
        super().__init__()
        self.setWindowTitle("Crash Log Viewer")
        self.setGeometry(300, 200, 700, 500)
        self.log_path = log_path
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("🛠 Crash/Error Logs:")
        layout.addWidget(self.label)

        self.log_viewer = QTextEdit()
        self.log_viewer.setReadOnly(True)
        layout.addWidget(self.log_viewer)

        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.clicked.connect(self.load_logs)
        layout.addWidget(refresh_btn)

        open_btn = QPushButton("📂 Open Different Log File")
        open_btn.clicked.connect(self.select_log_file)
        layout.addWidget(open_btn)

        self.setLayout(layout)
        self.load_logs()

    def load_logs(self):
        if os.path.exists(self.log_path):
            with open(self.log_path, "r", encoding="utf-8") as f:
                self.log_viewer.setText(f.read())
        else:
            self.log_viewer.setText("⚠️ No log file found at:
" + self.log_path)

    def select_log_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Log File", "logs/", "Text Files (*.txt)")
        if file_path:
            self.log_path = file_path
            self.load_logs()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = CrashLogViewer()
    viewer.show()
    sys.exit(app.exec_())