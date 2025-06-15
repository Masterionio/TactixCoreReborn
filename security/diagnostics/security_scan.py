import os
import hashlib

def hash_file(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def scan_for_dangerous_content(path):
    threats = ["eval(", "exec(", "import os", "base64,", "subprocess", "system("]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(('.py', '.sh', '.js', '.html')):
                full_path = os.path.join(root, file)
                with open(full_path, 'r', errors='ignore') as f:
                    content = f.read()
                    for t in threats:
                        if t in content:
                            print(f"[THREAT] {t} found in {full_path}")

def run_security_diagnostics():
    print("[SECURITY] Running Python security scan...")
    scan_for_dangerous_content(".")

run_security_diagnostics()
