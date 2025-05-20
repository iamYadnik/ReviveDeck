import sys
import platform
import shutil
import psutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit
)

class SystemInfoViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Info - ReviveDeck")
        self.setGeometry(300, 200, 600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.info_display = QTextEdit()
        self.info_display.setReadOnly(True)

        layout.addWidget(QLabel("🖥 System Information"))
        layout.addWidget(self.info_display)

        self.setLayout(layout)
        self.show_info()

    def show_info(self):
        info = []
        info.append(f"Platform: {platform.system()} {platform.release()}")
        info.append(f"Processor: {platform.processor()}")
        info.append(f"CPU Cores: {psutil.cpu_count(logical=True)}")
        info.append(f"Memory: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
        info.append(f"Disk Space: {round(shutil.disk_usage('/').total / (1024**3), 2)} GB total")

        self.info_display.setText("\n".join(info))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SystemInfoViewer()
    win.show()
    sys.exit(app.exec_())