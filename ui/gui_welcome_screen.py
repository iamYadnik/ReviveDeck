import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit
)
from PyQt5.QtGui import QFont
from config.theme_engine import load_theme_config, apply_theme

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to ReviveDeck!")
        self.setGeometry(300, 300, 600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        welcome = QLabel("🎉 Welcome to ReviveDeck")
        welcome.setFont(QFont("Arial", 18))
        layout.addWidget(welcome)

        message = QTextEdit()
        message.setReadOnly(True)
        message.setPlainText(
            "Thank you for installing ReviveDeck!

"
            "Here are some next steps you can take:
"
            "✅ Launch the dashboard to manage your games
"
            "🎨 Try switching between dark and light themes
"
            "🧩 Explore or install optional plugins
"
            "📦 Export and import profiles for easy backup

"
            "Have fun, and welcome to the community!"
        )
        layout.addWidget(message)

        button = QPushButton("Get Started")
        button.clicked.connect(self.close)
        layout.addWidget(button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    config = load_theme_config()
    apply_theme(app, config)
    win = WelcomeScreen()
    win.show()
    sys.exit(app.exec_())