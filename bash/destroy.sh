#!/bin/bash
# TactixCore - Secure Destroyer

if [ -z "$1" ]; then
  echo "[DESTROY] Usage: ./destroy.sh <filename>"
  exit 1
fi

if [ ! -f "$1" ]; then
  echo "[DESTROY] File not found."
  exit 1
fi

echo "[DESTROY] Secure deleting $1..."
shred -u -z -n 5 "$1"
echo "[DESTROY] Done. File permanently removed."
