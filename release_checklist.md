
# ✅ ReviveDeck Release Checklist

This document helps maintainers track tasks for new version releases.

---

## 📦 Version Bump

- [ ] Update version number in `__init__.py` or metadata
- [ ] Tag the version using Git:
  ```
  git tag -a vX.X.X -m "Release vX.X.X"
  git push origin vX.X.X
  ```

---

## 🧪 Testing

- [ ] Run `python scripts/task_scheduler.py`
- [ ] Verify launcher: `ui/unified_gui_launcher.py`
- [ ] Verify config editor, logger, and GUI dashboard
- [ ] Test backup/export and restore on a fresh machine
- [ ] Run Flatpak/AppImage build and confirm launch

---

## 🗃️ Files to Verify

- [ ] `launcher_config.json` loads and saves correctly
- [ ] `revivedeck_stats.json` updates with session tracking
- [ ] `game_profiles/` directory has valid `.json` files
- [ ] `revivedeck.log` and `diagnostic_report.md` generate as expected

---

## 🧾 Documentation

- [ ] Update `ROADMAP.md` if features are completed
- [ ] Update `tutorial.md` if commands, UI, or steps changed
- [ ] Confirm `CONTRIBUTING.md` and issue templates are current

---

## 🌐 Packaging

- [ ] AppImage bundles and launches via `.AppImage`
- [ ] Flatpak builds cleanly using `flatpak-builder`
- [ ] `README.md` reflects latest version and changelog

---

## 📣 Post-Release

- [ ] Announce new version in README, GitHub releases, and community channels
- [ ] Open new milestone for next version
- [ ] Archive prior release build (optional)

---

Made with ❤️ by the ReviveDeck maintainers.
