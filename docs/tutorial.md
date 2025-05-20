
# 📘 ReviveDeck User Tutorial

Welcome to ReviveDeck — an open-source runtime to launch and manage Steam Deck Verified games on any hardware.

---

## 🚀 Getting Started

1. **Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/ReviveDeck.git
cd ReviveDeck
```

2. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Unified Launcher**
```bash
python ui/unified_gui_launcher.py
```

4. **Or Open the Dashboard**
```bash
python ui/gui_home_dashboard.py
```

---

## 🛠 Key Features

### 🎮 Launch & Manage Games
Use the unified GUI to manage game profiles, settings, and launchers.

### 📊 Track Usage
Use `gui_stats_dashboard.py` to monitor playtime, launches, and more.

### 🔄 Sync Steam Metadata
Run `steam_api_integrator.py` to pull your Steam games and artwork:
```bash
python scripts/steam_api_integrator.py
```

### 🗃 Backup & Restore
Create or restore your settings archive:
```bash
python scripts/backup_manager.py
```

### 🧾 Compare Profiles
Launch the profile diff viewer to check what's changed:
```bash
python ui/gui_profile_diff_viewer.py
```

---

## 🔁 Customization

- 🎨 Icons & splash screens are in `assets/`
- 🔧 Configs and logs are in the root directory
- 🧹 Reset the environment via:
```bash
python scripts/reset_cleaner.py
```

---

## 🧑‍💻 Developer Utilities

- Use `task_scheduler.py` to run diagnostics & automation
- Run lint checks with GitHub Actions CI

---

## 📦 Packaging Options

- Use `appimage_bundler.py` for AppImage builds
- Use `flatpak_manifest.json` for Flatpak + Flathub

---

For any issues, please check `CONTRIBUTORS.md` or open a GitHub Issue.

_Thanks for supporting accessible gaming for all 🕹_
