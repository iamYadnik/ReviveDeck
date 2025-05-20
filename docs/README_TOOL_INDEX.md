# 🧰 ReviveDeck Tools & Utilities Index

This document provides an overview of all core modules, GUIs, and utility scripts included in the ReviveDeck ecosystem.

---

## 🖥 GUI Tools (`/ui`)

| Tool | Description |
|------|-------------|
| `gui_home_dashboard.py` | Central launcher for all ReviveDeck tools |
| `gui_welcome_screen.py` | First-time user onboarding screen |
| `gui_settings_manager.py` | Change and save theme preferences |
| `gui_profile_manager.py` | Manage multiple user profiles |
| `gui_feature_toggle_manager.py` | Enable/disable optional features |
| `gui_backup_restore.py` | Backup and restore your config folder |
| `gui_stats_dashboard.py` | View gameplay stats and usage |
| `gui_diagnostic_log_viewer.py` | Searchable view of app logs |
| `gui_module_boilerplate.py` | Starter template for custom modules |
| `theme_preview_tool.py` | Preview and apply dark/light themes |
| `profile_switcher_widget.py` | Embeddable profile switcher for dashboards |

---

## ⚙️ Scripts & Background Jobs (`/scripts`)

| Script | Description |
|--------|-------------|
| `usage_stats_exporter.py` | Export usage data to CSV and Excel |
| `backup_manager.py` | Backup utility for config and settings |
| `steam_api_integrator.py` | Pull data from your Steam library |
| `release_notes_generator.py` | Extract latest changelog as release notes |
| `cron_task_runner.py` | Auto-run tasks like export or validate at intervals |
| `module_dependency_checker.py` | Scan and validate plugin/script imports |

---

## 🔌 Plugins (`/plugins`)

| File | Description |
|------|-------------|
| `plugin_loader.py` | Dynamically loads all valid plugins |
| `plugin_validator.py` | Checks structure and safety of plugins |
| `plugin_template.py` | Boilerplate for creating a new plugin |
| `hello_world.py` | Minimal working plugin example |

---

## 📚 Docs & Developer Files (`/docs`)

| File | Description |
|------|-------------|
| `tutorial.md` | Full user guide |
| `github_release_checklist.md` | Pre-release checklist for maintainers |
| `plugin_marketplace_vision.md` | Roadmap for plugin ecosystem |
| `CONTRIBUTING_PLUGIN.md` | Guide for developers submitting plugins |

---

## 🏁 Other Entry Points

| File | Description |
|------|-------------|
| `launcher_wrapper.py` | Opens splash → dashboard on startup |
| `first_run_welcome.py` | Displays welcome screen on first launch |
| `feature_toggles.json` | Toggle individual tools or features |

---

_Keep building. Keep sharing. The platform is yours._