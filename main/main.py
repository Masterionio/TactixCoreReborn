# main.py – Python Entrypoint for TactixCore Reborn
import subprocess
import json
import yaml

def load_json(path="main.json"):
    with open(path, "r") as f:
        return json.load(f)

def load_yaml(path="main.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def start_shell():
    print("🧪 Launching TactixCore system via index.shell...")
    subprocess.call(["bash", "index.shell"])

def main():
    meta = load_json()
    settings = load_yaml()

    print(f"\n🧠 {meta['app_name']} v{meta['version']} — Master Control")
    print("🛠 Status:", "Safe" if settings['safe_mode'] else "Custom Risk Mode")

    if settings.get("auto_start_index"):
        start_shell()
    else:
        print("🕹 Manual mode active. Run `index.shell` to launch.")

if __name__ == "__main__":
    main()
