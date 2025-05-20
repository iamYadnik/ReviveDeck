import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox,
    QTextEdit, QPushButton, QMessageBox
)

class PostInstallChecklist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Post-Install Checklist & Feedback")
        self.setGeometry(300, 250, 600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("✅ Welcome to ReviveDeck! Here's what you can do next:"))

        self.steps = {
            "theme": QCheckBox("Set your preferred theme (dark/light/custom)"),
            "profile": QCheckBox("Create a user profile"),
            "dashboard": QCheckBox("Launch the Dashboard"),
            "plugins": QCheckBox("Load or write your first plugin"),
            "backup": QCheckBox("Create a backup of your config")
        }

        for checkbox in self.steps.values():
            layout.addWidget(checkbox)

        layout.addWidget(QLabel("💬 We'd love your feedback:"))
        self.feedback_input = QTextEdit()
        self.feedback_input.setPlaceholderText("Write any feedback, suggestions, or bugs here...")
        layout.addWidget(self.feedback_input)

        submit_btn = QPushButton("Submit Feedback")
        submit_btn.clicked.connect(self.submit_feedback)
        layout.addWidget(submit_btn)

        self.setLayout(layout)

    def submit_feedback(self):
        feedback = self.feedback_input.toPlainText().strip()
        completed = [key for key, cb in self.steps.items() if cb.isChecked()]
        if feedback or completed:
            print("🎉 Post-install checklist completed:")
            for item in completed:
                print(f" - {item}")
            print("📝 Feedback submitted:")
            print(feedback)
            QMessageBox.information(self, "Thank You!", "✅ Your feedback was submitted!")
            self.close()
        else:
            QMessageBox.warning(self, "Nothing to submit", "⚠️ Please check at least one item or enter feedback.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PostInstallChecklist()
    win.show()
    sys.exit(app.exec_())