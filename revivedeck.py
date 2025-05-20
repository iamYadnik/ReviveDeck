import argparse
import subprocess

TOOLS = {
    "dashboard": "ui/gui_home_dashboard.py",
    "welcome": "ui/gui_welcome_screen.py",
    "settings": "ui/gui_settings_manager.py",
    "profiles": "ui/gui_profile_manager.py",
    "features": "ui/gui_feature_toggle_manager.py",
    "backup": "ui/gui_backup_restore.py",
    "stats": "ui/gui_stats_dashboard.py",
    "logs": "ui/gui_diagnostic_log_viewer.py",
    "sysinfo": "ui/gui_system_info.py",
    "preview": "ui/theme_preview_tool.py",
    "switcher": "ui/profile_switcher_widget.py",
    "export": "scripts/usage_stats_exporter.py",
    "validate": "plugin_validator.py",
    "load_plugins": "plugin_loader.py",
    "run_cron": "scripts/cron_task_runner.py"
}

def launch_tool(tool_name):
    script = TOOLS.get(tool_name)
    if not script:
        print(f"❌ Unknown tool: {tool_name}")
        return
    print(f"🚀 Launching: {tool_name}")
    subprocess.run(["python", script])

def main():
    parser = argparse.ArgumentParser(description="ReviveDeck CLI Launcher")
    parser.add_argument("tool", help="Tool to launch (e.g., dashboard, backup, sysinfo)")
    args = parser.parse_args()
    launch_tool(args.tool)

if __name__ == "__main__":
    main()