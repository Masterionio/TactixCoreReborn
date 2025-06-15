#!/bin/bash
# TactixCore - Bash Troubleshooter

echo "[TROUBLESHOOT] Running diagnostics..."

echo "1. Checking disk space..."
df -h

echo "2. Checking RAM usage..."
free -m

echo "3. Checking internet connection..."
ping -c 2 8.8.8.8 >/dev/null && echo "✅ Online" || echo "❌ Offline"

echo "4. Scanning logs for errors..."
grep -i "error" logs/*.log

echo "[TROUBLESHOOT] Done."
