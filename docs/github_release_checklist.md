# 🚀 GitHub Release Checklist

Use this guide to prepare a clean, professional GitHub release for ReviveDeck.

---

## 📦 Pre-Release Preparation

- [ ] All tests pass (CI green)
- [ ] All new features documented in `CHANGELOG.md`
- [ ] `version` field updated in code (if applicable)
- [ ] Update any related screenshots, README, or assets
- [ ] Run plugin validator and theme preview for visual QA

---

## 🧾 Files to Include

- [ ] `AppImage` or `Flatpak` build file
- [ ] Latest `LICENSE`, `README.md`, and `ROADMAP.md`
- [ ] All `.json` config templates (themes, i18n)
- [ ] Exported ZIP of full source code or GitHub auto-zip

---

## 📝 Create the Release

1. Go to: [GitHub Releases](https://github.com/YOUR_USERNAME/ReviveDeck/releases)
2. Click `Draft a new release`
3. Choose a tag version (e.g. `v1.0.0`)
4. Fill out release title and description:
   - Summary of new features
   - Highlights from `CHANGELOG.md`
   - Known issues (optional)
5. Upload any binaries or installer files
6. Click `Publish release`

---

## 📣 Post-Release

- [ ] Announce on GitHub Discussions (if enabled)
- [ ] Share in README, Discord, or website
- [ ] Open new milestone for next version
- [ ] Tidy up any open pull requests linked to previous milestone

---

_Made with 💡 by the ReviveDeck maintainers._