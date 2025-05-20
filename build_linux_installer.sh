#!/bin/bash

APP_NAME="ReviveDeck"
INSTALL_DIR="$HOME/.revivedeck"
LAUNCHER="$HOME/.local/bin/revivedeck"

echo "🐧 Installing $APP_NAME to $INSTALL_DIR..."

mkdir -p "$INSTALL_DIR"
mkdir -p "$HOME/.local/bin"

cp -r ui config scripts plugins assets revivedeck.py "$INSTALL_DIR"

echo "#!/bin/bash" > "$LAUNCHER"
echo "python3 $INSTALL_DIR/revivedeck.py" >> "$LAUNCHER"
chmod +x "$LAUNCHER"

echo "✅ $APP_NAME installed."
echo "➡️  Run it anytime by typing: revivedeck"