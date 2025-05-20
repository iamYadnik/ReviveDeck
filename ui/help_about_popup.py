from PyQt5.QtWidgets import QMessageBox

def show_about(parent=None):
    QMessageBox.information(
        parent,
        "About ReviveDeck",
        (
            "<h2>ReviveDeck</h2>"
            "<p>ReviveDeck is a cross-platform runtime for playing Steam Deck Verified games "
            "on any hardware. It is open-source and fully modular, with support for configuration management, "
            "game telemetry, and UI customization.</p>"
            "<p><b>Version:</b> 0.9.x<br>"
            "<b>Author:</b> ReviveDeck Contributors<br>"
            "<b>License:</b> MIT</p>"
            "<p>GitHub: <a href='https://github.com/YOUR_USERNAME/ReviveDeck'>ReviveDeck</a></p>"
        )
    )