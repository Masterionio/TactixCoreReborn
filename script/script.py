# script.py — Python sample that uses config.py

from config.config import Config

def display_status():
    print(f"Welcome to {Config.APP_NAME} v{Config.VERSION}")
    print(f"Theme set to: {Config.THEME}")
    print("Modules enabled:")
    if Config.FIREWALL_ENABLE_MONITORING:
        print("- Firewall Monitor")
    if Config.AUTO_START_INDEX:
        print("- Auto-start index enabled")
    # Add more as needed

if __name__ == "__main__":
    display_status()
