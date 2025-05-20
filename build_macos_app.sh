#!/bin/bash

APP_NAME="ReviveDeck"
MAIN_SCRIPT="revivedeck.py"
ICON_PATH="assets/revivedeck_icon.icns"

echo "🍏 Building $APP_NAME macOS .app bundle..."

if [ ! -f "$MAIN_SCRIPT" ]; then
    echo "❌ Main script $MAIN_SCRIPT not found."
    exit 1
fi

if [ ! -f "$ICON_PATH" ]; then
    echo "⚠️ Icon file not found at $ICON_PATH. Continuing without icon."
    ICON_FLAG=""
else
    ICON_FLAG="--icon $ICON_PATH"
fi

pyinstaller \
    --windowed \
    --onefile \
    $ICON_FLAG \
    --name "$APP_NAME" \
    "$MAIN_SCRIPT"

echo "✅ macOS .app build complete. Check dist/ directory."