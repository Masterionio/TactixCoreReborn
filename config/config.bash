#!/bin/bash
# config.bash — TactixCore config as shell variables

export APP_NAME="TactixCore Reborn"
export VERSION="1.0.0"
export THEME="bitdefender-dark"
export AUTO_START_INDEX=true
export SAFE_MODE=true

export DEFAULT_MODE="AI Optimized"
export AUTO_OPTIMIZE_EVERY=5
export CACHE_CLEAR_ON_START=true

export HEURISTIC_DETECTION=true
export REALTIME_PROTECTION=true
export SCAN_EXTENSIONS="exe dll sys js py"

export QUARANTINE_PATH="quarantine/"
export MAX_DAYS_TO_KEEP=30
export AUTO_DELETE_DANGEROUS=true
export REVIEW_BEFORE_DELETION=true

export FIREWALL_ENABLE_MONITORING=true
export FIREWALL_BLOCK_SUSPICIOUS_PORTS=true
export TRUSTED_IPS="127.0.0.1 ::1 192.168.1.1"
export BLOCKED_IPS="13.66.58.251 45.13.253.23"

export LOGGING_ENABLE=true
export LOG_FOLDER="logs/"
export LOG_LEVEL="INFO"
