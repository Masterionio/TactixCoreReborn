#!/bin/bash

CACHE_DIR="./cache"

echo "[CACHEGUARD] Locking and checking cache folder..."

if [ ! -d "$CACHE_DIR" ]; then
  echo "Cache folder not found."
  exit 1
fi

for file in "$CACHE_DIR"/*; do
  case "$file" in
    *.tmp|*.log|*.cache|*.txt)
      chmod 400 "$file"
      echo "[✓] Locked safe file: $file"
      ;;
    *)
      echo "[!] Suspicious file: $file — moved to quarantine."
      mv "$file" ./quarantine/
      ;;
  esac
done
