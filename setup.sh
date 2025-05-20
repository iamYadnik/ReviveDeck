#!/bin/bash

echo "🔧 Setting up ReviveDeck environment..."

# Create folders if they don't exist
mkdir -p game_profiles
mkdir -p test_configs
mkdir -p scripts
mkdir -p ui

# Install required Python packages
echo "📦 Installing Python dependencies..."
pip install pyqt5 psutil

# Download sample launcher config
if [ ! -f launcher_config.json ]; then
  echo "Creating default launcher_config.json..."
  cat <<EOF > launcher_config.json
{
    "preferred_resolution": "1280x720",
    "fps_cap": 30,
    "vsync": false,
    "language": "en",
    "theme": "dark",
    "auto_optimize": true,
    "game_install_path": "/home/user/.steam/steam/steamapps/common/"
}
EOF
fi

echo "✅ Setup complete. You're ready to launch ReviveDeck!"
