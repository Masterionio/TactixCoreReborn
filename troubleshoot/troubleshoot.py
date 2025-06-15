import os
import shutil
import socket
import psutil

print("[TROUBLESHOOT] Running Python diagnostics...")

print("1. Disk space:", shutil.disk_usage("/"))
print("2. RAM:", psutil.virtual_memory())
print("3. Hostname:", socket.gethostname())
print("4. Internet:", "Online" if socket.gethostbyname("google.com") else "Offline")

print("[TROUBLESHOOT] Done.")
