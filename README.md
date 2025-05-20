
# ReviveDeck

**ReviveDeck** is a cross-platform, open-source runtime and launcher designed to make Steam Deck Verified games playable on any hardware — from low-end legacy PCs to Android tablets.

## 💡 Vision

> Bring the Steam Deck experience to every device — without needing a Steam Deck.

## 🔧 Project Structure

```
ReviveDeck/
├── game_profiles/               # Optimization profiles (per game)
├── scripts/                     # CLI tools and system scripts
├── test_configs/                # Sample INI/CFG files for testing
├── ui/                          # GUI Launcher files
├── launcher_config.json         # Global user config
├── setup.sh                     # Environment setup script
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ReviveDeck.git
cd ReviveDeck
```

### 2. Run the Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

---

## 🛠️ Modules & Tools

### 🔹 `revivedeck_launcher.py`
Basic CLI launcher to select and run installed Steam games via Proton.

### 🔹 `game_optimizer.py`
Applies game-specific performance tweaks to `.ini` or `.cfg` files.

### 🔹 `config_reader.py`
Reads global launcher preferences from `launcher_config.json`.

### 🔹 `hardware_detect.py`
Prints CPU, RAM, and disk info for performance profiling.

### 🔹 `game_profile_editor.py`
Creates `.json` optimization profiles interactively via terminal.

### 🔹 `test_optimizer_runner.py`
Runs the optimizer on test config files to verify functionality.

### 🔹 `ui_launcher_stub.py`
Minimal PyQt5 GUI to simulate game selection and launching.

---

## 🧪 Testing

To test config optimization:
```bash
python scripts/test_optimizer_runner.py
```

To open GUI:
```bash
python ui/ui_launcher_stub.py
```

---

## 📜 License

MIT License

---

Made with ❤️ by gamers, for gamers.
