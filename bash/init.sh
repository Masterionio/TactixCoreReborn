#!/bin/bash
# TactixCore Reborn - Initializer

echo "[INIT] Starting TactixCore setup..."
mkdir -p logs config cache temp

echo "[INIT] Setting file permissions..."
chmod -R 755 ./config
chmod -R 700 ./logs
chmod +x ./bash/*.sh

echo "[INIT] Setup complete. Ready to launch."
