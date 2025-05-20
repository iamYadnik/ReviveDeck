import subprocess
import time

def run_splash_and_dashboard():
    try:
        # Launch splash screen
        splash = subprocess.Popen(["python", "ui/splash_loader_overlay.py"])
        splash.wait()  # Wait until splash closes (simulated loading ends)

        # Then launch the dashboard
        subprocess.Popen(["python", "ui/gui_home_dashboard.py"])

    except Exception as e:
        print(f"❌ Failed to run launcher wrapper: {e}")

if __name__ == "__main__":
    run_splash_and_dashboard()