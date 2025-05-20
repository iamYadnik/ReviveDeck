
import os
import json
import platform
import psutil
from datetime import datetime

def gather_system_info():
    return {
        "Processor": platform.processor(),
        "Architecture": platform.machine(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "Total RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Total Disk Space (GB)": round(psutil.disk_usage('/').total / (1024 ** 3), 2),
        "Platform": platform.system(),
        "Platform Version": platform.version()
    }

def load_launcher_config(config_path="launcher_config.json"):
    if not os.path.exists(config_path):
        return {}
    with open(config_path, "r") as f:
        return json.load(f)

def generate_report(output_path="diagnostic_report.md"):
    sys_info = gather_system_info()
    config = load_launcher_config()

    with open(output_path, "w") as f:
        f.write(f"# 🖥️ ReviveDeck Diagnostic Report\n")
        f.write(f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## 🔧 System Info\n")
        for key, val in sys_info.items():
            f.write(f"- **{key}:** {val}\n")

        f.write("\n## ⚙️ Launcher Configuration\n")
        for key, val in config.items():
            f.write(f"- **{key}:** {val}\n")

        f.write("\n✅ Report generation complete.\n")

    print(f"Diagnostic report saved to {output_path}")

if __name__ == "__main__":
    generate_report()
