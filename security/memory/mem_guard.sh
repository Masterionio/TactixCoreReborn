#!/bin/bash
echo "[BASH] Checking system memory..."

free -h
echo ""
echo "[BASH] Top memory-hungry processes:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 10
