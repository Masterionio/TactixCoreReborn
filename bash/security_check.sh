#!/bin/bash
# TactixCore Reborn - Basic Security Check

echo "[SECURITY] Checking for suspicious executables..."
find . -type f -exec file {} \; | grep "executable"

echo "[SECURITY] Active network ports:"
netstat -tulnp | grep LISTEN

echo "[SECURITY] Done."
