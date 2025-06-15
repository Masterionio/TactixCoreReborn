import logging
import json
from datetime import datetime

# Setup basic logger
logging.basicConfig(filename='debug.log', level=logging.DEBUG, 
                    format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def log_info(msg):
    logging.info(msg)
    update_json_log("INFO", msg)

def log_error(msg):
    logging.error(msg)
    update_json_log("ERROR", msg)

def update_json_log(level, msg):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "message": msg
    }
    try:
        with open('debug.json', 'r+') as f:
            data = json.load(f)
            data["logs"].append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('debug.json', 'w') as f:
            json.dump({"logs": [log_entry]}, f, indent=2)

if __name__ == "__main__":
    log_info("TactixCore debugging initialized.")
    log_error("Sample error logged for testing.")
