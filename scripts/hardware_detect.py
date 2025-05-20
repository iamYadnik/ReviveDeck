
import platform
import psutil
import shutil

def get_system_info():
    info = {}

    # CPU info
    info['Processor'] = platform.processor()
    info['Architecture'] = platform.machine()
    info['CPU Cores'] = psutil.cpu_count(logical=False)
    info['Logical CPUs'] = psutil.cpu_count(logical=True)

    # RAM info
    total_memory = psutil.virtual_memory().total
    info['Total RAM (GB)'] = round(total_memory / (1024 ** 3), 2)

    # Disk info
    total_disk = shutil.disk_usage("/").total
    info['Total Disk Space (GB)'] = round(total_disk / (1024 ** 3), 2)

    return info

def print_system_info():
    info = get_system_info()
    print("=== System Info ===")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print_system_info()
