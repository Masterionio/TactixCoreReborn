#!/bin/bash
# TactixCore Reborn - Cleaner Script

echo "[CLEAN] Wiping cache and temp files..."
rm -rf cache/* temp/*

echo "[CLEAN] Old logs? (y/N)"
read confirm
if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
  rm -f logs/*
  echo "[CLEAN] Logs deleted."
else
  echo "[CLEAN] Skipped log cleanup."
fi

echo "[CLEAN] Done."
