import os
import hashlib
import shutil

CACHE_PATH = "./cache"
SAFE_EXTENSIONS = [".tmp", ".log", ".cache", ".txt"]

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def is_safe_file(filename):
    return any(filename.endswith(ext) for ext in SAFE_EXTENSIONS)

def scan_cache():
    print("[CACHEGUARD] Scanning cache folder...")
    if not os.path.exists(CACHE_PATH):
        print("No cache folder found.")
        return

    for file in os.listdir(CACHE_PATH):
        file_path = os.path.join(CACHE_PATH, file)
        if not is_safe_file(file):
            print(f"[!] Suspicious file: {file_path} - Quarantining.")
            shutil.move(file_path, f"./quarantine/{file}")
        else:
            print(f"[✓] Safe: {file_path} – Hash: {hash_file(file_path)[:16]}...")

def clear_cache():
    print("[CACHEGUARD] Clearing all safe cache...")
    for file in os.listdir(CACHE_PATH):
        file_path = os.path.join(CACHE_PATH, file)
        if is_safe_file(file):
            os.remove(file_path)
    print("[CACHEGUARD] Cache cleared.")

scan_cache()
clear_cache()
