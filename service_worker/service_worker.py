# service_worker.py
import os
import time

CACHE = {}
CACHE_NAME = "tactixcore-cache-v1"

def cache_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            CACHE[file_path] = f.read()
        print(f"Cached: {file_path}")
    else:
        print(f"File not found, cannot cache: {file_path}")

def cache_static_assets():
    assets = [
        'index.html',
        'script.js',
        'style.css',
        'config/config.ini',
        'config/config.py',
    ]
    for asset in assets:
        cache_file(asset)

def fetch_from_cache(request):
    if request in CACHE:
        print(f"Serving from cache: {request}")
        return CACHE[request]
    else:
        print(f"Cache miss: {request}, fetching fresh...")
        # In real SW, fetch from network here
        return None

def update_cache():
    print("Updating cache...")
    cache_static_assets()
    print("Cache updated.")

if __name__ == "__main__":
    print("Service Worker (simulated) starting...")
    update_cache()
    # Simulate fetch event
    fetch_from_cache('index.html')
    time.sleep(2)
    fetch_from_cache('unknown.file')
