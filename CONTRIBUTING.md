
# 🤝 Contributing to ReviveDeck

Thanks for your interest in contributing to **ReviveDeck** — an open-source initiative to bring Steam Deck Verified gaming to any hardware.

We welcome developers, designers, testers, writers, and enthusiasts from all skill levels.

---

## 🛠️ How to Contribute

### 1. Fork the Repository
Click the "Fork" button on the top-right corner of the GitHub page to create your own copy.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/ReviveDeck.git
cd ReviveDeck
```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
Follow the project structure and keep code clean and modular.

### 5. Test Your Changes
Run the relevant modules:
```bash
python scripts/test_optimizer_runner.py
python ui/ui_launcher_integrated.py
```

### 6. Commit & Push
```bash
git add .
git commit -m "Add: [your description]"
git push origin feature/your-feature-name
```

### 7. Submit a Pull Request
Go to your fork on GitHub → "Compare & Pull Request" → Write a brief explanation.

---

## 📦 Contributing Areas

- **Python Devs:** CLI tools, file parsers, config logic
- **UI Designers:** Build GUI in PyQt, Tauri, or Electron
- **Game Testers:** Test optimizer against real games
- **Writers:** Tutorials, Docs, Translations

---

## 🧠 Guidelines

- Follow PEP8 for Python code
- Use clear commit messages
- Add docstrings for custom functions
- Respect directory structure
- Avoid hardcoding paths (use config whenever possible)

---

## 💬 Community

Join our [Discord server]() to collaborate, ask questions, and stay updated.

---

Let’s build the “Steam Deck for Everyone” — together.

—
ReviveDeck Maintainers
