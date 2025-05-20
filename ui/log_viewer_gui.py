
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton

LOG_FILE = "revivedeck.log"

class LogViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Log Viewer")
        self.setGeometry(150, 150, 700, 500)
        self.setup_ui()
        self.load_log()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        self.refresh_button = QPushButton("Refresh Log")
        self.refresh_button.clicked.connect(self.load_log)
        layout.addWidget(self.refresh_button)

        self.setLayout(layout)

    def load_log(self):
        try:
            with open(LOG_FILE, "r") as f:
                content = f.read()
            self.text_area.setPlainText(content)
        except FileNotFoundError:
            self.text_area.setPlainText("No log file found.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = LogViewer()
    viewer.show()
    sys.exit(app.exec_())
