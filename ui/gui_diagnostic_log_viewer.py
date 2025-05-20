import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont

LOG_FILE = "revivedeck.log"

class DiagnosticLogViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Diagnostic Log Viewer")
        self.setGeometry(300, 200, 800, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title = QLabel("📄 Diagnostic Log Viewer")
        self.title.setFont(QFont("Arial", 16))
        layout.addWidget(self.title)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search log text...")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_text)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        self.text_area = QTextEdit()
        self.text_area.setFont(QFont("Courier", 10))
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        self.setLayout(layout)
        self.load_log()

    def load_log(self):
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                content = f.read()
                self.text_area.setPlainText(content)
        else:
            QMessageBox.warning(self, "Missing File", f"Log file not found: {LOG_FILE}")

    def search_text(self):
        search_term = self.search_input.text().strip()
        if search_term:
            cursor = self.text_area.textCursor()
            document = self.text_area.document()
            found = False
            cursor.beginEditBlock()
            cursor.setPosition(0)
            while True:
                cursor = document.find(search_term, cursor)
                if cursor.isNull():
                    break
                self.text_area.setTextCursor(cursor)
                found = True
                break
            cursor.endEditBlock()
            if not found:
                QMessageBox.information(self, "Search", f"'{search_term}' not found in log.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = DiagnosticLogViewer()
    viewer.show()
    sys.exit(app.exec_())