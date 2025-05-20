# 🧩 Contributing Plugins to ReviveDeck

Thank you for your interest in developing a plugin for ReviveDeck!

This guide outlines how to build, structure, and submit your plugin.

---

## 📦 Folder Structure

All plugins must go inside the `plugins/` directory:

```
ReviveDeck/
├── plugins/
│   ├── my_awesome_plugin.py
```

---

## 🔧 Plugin Requirements

Each plugin must:
- Be a standalone `.py` file
- Contain a `register()` function (called during load)
- Avoid importing GUI modules unless needed
- Handle exceptions internally and fail gracefully

```python
def register():
    print("✅ Plugin registered!")
```

---

## 📝 Recommended Plugin Metadata

(Optional) Include a `plugin.json` with your `.py` file:

```json
{
  "name": "My Awesome Plugin",
  "version": "1.0.0",
  "description": "Adds FPS overlay and telemetry.",
  "author": "yourname",
  "license": "MIT"
}
```

---

## 🧪 Local Testing

To validate your plugin:

1. Run the validator:
```bash
python plugin_validator.py
```

2. Load the plugin:
```bash
python plugin_loader.py
```

3. Or add it to your launcher wrapper or dashboard.

---

## 💡 Plugin Ideas

- Config optimizers
- Replay logger
- Launcher themes
- Accessibility modules
- Save file syncers

---

## ✅ Submitting a Plugin

1. Fork the repository
2. Add your `.py` and (optional) `plugin.json` to `/plugins`
3. Submit a pull request with:
   - A short README or docstring
   - Screenshot (if applicable)
   - Clear purpose and usage

---

## 📢 Notes

- Plugins must be MIT/GPL licensed
- No malicious code or telemetry allowed
- Community-reviewed before acceptance

---

Let’s make ReviveDeck the most flexible game platform together 🎮