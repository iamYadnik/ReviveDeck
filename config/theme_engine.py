import json
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QFile, QTextStream

def load_theme_config(path="config/theme_config.json"):
    with open(path, "r") as f:
        return json.load(f)

def apply_theme(app, config, mode=None):
    theme = config["theme"] if mode is None else mode
    colors = config.get(theme, {})

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(colors.get("background", "#ffffff")))
    palette.setColor(QPalette.WindowText, QColor(colors.get("foreground", "#000000")))
    palette.setColor(QPalette.Base, QColor(colors.get("background", "#ffffff")))
    palette.setColor(QPalette.Text, QColor(colors.get("foreground", "#000000")))
    palette.setColor(QPalette.Button, QColor(colors.get("button", "#cccccc")))
    palette.setColor(QPalette.ButtonText, QColor(colors.get("foreground", "#000000")))
    palette.setColor(QPalette.Highlight, QColor(colors.get("highlight", "#0078d7")))
    palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))

    app.setPalette(palette)

    return palette  # optional

# Example usage in a PyQt5 GUI:
# from theme_engine import load_theme_config, apply_theme
# app = QApplication(sys.argv)
# config = load_theme_config()
# apply_theme(app, config)