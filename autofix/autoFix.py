import os
import shutil

print("[AUTOFIX] Running auto-fixes...")

# Clear cache
cache_path = "./cache"
if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
    os.mkdir(cache_path)

# Fix permissions
os.system("chmod -R 755 ./")

print("[AUTOFIX] Fixes applied successfully.")
