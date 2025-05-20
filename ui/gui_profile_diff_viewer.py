
import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,
    QFileDialog, QMessageBox, QHBoxLayout
)
from difflib import unified_diff

class ProfileDiffViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ReviveDeck Profile Diff Viewer")
        self.setGeometry(200, 200, 900, 600)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.info_label = QLabel("Compare two JSON profile files")
        layout.addWidget(self.info_label)

        btn_layout = QHBoxLayout()
        self.btn_load_1 = QPushButton("Select Profile 1")
        self.btn_load_1.clicked.connect(lambda: self.load_file(1))
        self.btn_load_2 = QPushButton("Select Profile 2")
        self.btn_load_2.clicked.connect(lambda: self.load_file(2))
        btn_layout.addWidget(self.btn_load_1)
        btn_layout.addWidget(self.btn_load_2)
        layout.addLayout(btn_layout)

        self.diff_display = QTextEdit()
        self.diff_display.setReadOnly(True)
        layout.addWidget(self.diff_display)

        self.setLayout(layout)
        self.file1 = None
        self.file2 = None

    def load_file(self, file_num):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select JSON Profile", "", "JSON Files (*.json)")
        if file_path:
            if file_num == 1:
                self.file1 = file_path
            else:
                self.file2 = file_path
            self.compare_files()

    def compare_files(self):
        if not self.file1 or not self.file2:
            return

        try:
            with open(self.file1, 'r') as f1, open(self.file2, 'r') as f2:
                data1 = json.dumps(json.load(f1), indent=4).splitlines(keepends=True)
                data2 = json.dumps(json.load(f2), indent=4).splitlines(keepends=True)

            diff = unified_diff(
                data1, data2,
                fromfile=os.path.basename(self.file1),
                tofile=os.path.basename(self.file2),
                lineterm=""
            )

            diff_output = "".join(diff)
            self.diff_display.setPlainText(diff_output if diff_output else "✅ Profiles are identical.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to compare files:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ProfileDiffViewer()
    viewer.show()
    sys.exit(app.exec_())
