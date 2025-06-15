import xml.etree.ElementTree as ET
import hashlib
import os

def get_sha256(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def check_integrity():
    tree = ET.parse('security_diagnostics/verify_integrity.xml')
    root = tree.getroot()
    print("[XML] Checking file hashes against definitions...")

    for item in root.findall('check'):
        file = item.get('file')
        expected = item.get('hash')
        actual = get_sha256(file)

        if actual is None:
            print(f"[X] File missing: {file}")
        elif actual != expected:
            print(f"[!] HASH MISMATCH for {file}")
            print(f"    Expected: {expected}")
            print(f"    Actual:   {actual}")
        else:
            print(f"[✓] {file} integrity verified.")

check_integrity()
