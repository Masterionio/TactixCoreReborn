# config.py — TactixCore Reborn configuration in Python

class Config:
    APP_NAME = "TactixCore Reborn"
    VERSION = "1.0.0"
    THEME = "bitdefender-dark"
    AUTO_START_INDEX = True
    SAFE_MODE = True

    DEFAULT_MODE = "AI Optimized"
    AUTO_OPTIMIZE_EVERY = 5  # minutes
    CACHE_CLEAR_ON_START = True

    HEURISTIC_DETECTION = True
    REALTIME_PROTECTION = True
    SCAN_EXTENSIONS = ["exe", "dll", "sys", "js", "py"]

    QUARANTINE_PATH = "quarantine/"
    MAX_DAYS_TO_KEEP = 30
    AUTO_DELETE_DANGEROUS = True
    REVIEW_BEFORE_DELETION = True

    FIREWALL_ENABLE_MONITORING = True
    FIREWALL_BLOCK_SUSPICIOUS_PORTS = True
    TRUSTED_IPS = ["127.0.0.1", "::1", "192.168.1.1"]
    BLOCKED_IPS = ["13.66.58.251", "45.13.253.23"]

    LOGGING_ENABLE = True
    LOG_FOLDER = "logs/"
    LOG_LEVEL = "INFO"
