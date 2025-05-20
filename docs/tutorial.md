
# 🎮 ReviveDeck Tutorial

Welcome to the official **ReviveDeck** tutorial. This guide will walk you through setting up the project, running the tools, and contributing to the open-source effort.

---

## ✅ 1. Clone the Project

```bash
git clone https://github.com/YOUR_USERNAME/ReviveDeck.git
cd ReviveDeck
```

---

## ⚙️ 2. Run Setup Script

```bash
chmod +x setup.sh
./setup.sh
```

This installs required dependencies and sets up initial folders like:

- `game_profiles/`
- `scripts/`
- `ui/`
- `test_configs/`

---

## 🔧 3. Create a Game Profile

```bash
python scripts/game_profile_editor.py
```

Follow the prompts to generate a `.json` optimization profile.

---

## 🛠️ 4. Test Optimization on Configs

Make sure you have sample files in `test_configs/`, then run:

```bash
python scripts/test_optimizer_runner.py
```

Check if the `.ini` or `.cfg` files were optimized correctly.

---

## 🖥️ 5. Launch GUI Interface

```bash
python ui/ui_launcher_integrated.py
```

Select and launch a game (simulation for now). This interface reads from:

- `launcher_config.json`
- `game_profiles/`
- Logs actions in `revivedeck.log`

---

## 📤 6. Contribute or Customize

You can modify any part of the code and submit pull requests. Start here:

- `scripts/` → Core logic tools
- `ui/` → GUI launcher
- `docs/` → Tutorials and guides

---

## 💬 Need Help?

Join the community on Discord or post issues on GitHub.

Together, we’re building the Steam Deck experience for everyone.

---

Made with ❤️ by the ReviveDeck community.
