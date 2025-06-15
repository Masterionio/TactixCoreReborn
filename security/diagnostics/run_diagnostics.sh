#!/bin/bash

echo "[DIAGNOSTICS] Starting TactixCore Security Diagnostics..."

# Step 1: Python file scanner
echo "[PY] Running script scan..."
python3 security_diagnostics/security_scan.py >> security_diagnostics/security_alert.log

# Step 2: Audit file permissions
echo "[SH] Auditing file permissions..."
bash security_diagnostics/audit_permissions.sh >> security_diagnostics/security_alert.log

# Step 3: Run C++ suspicious process scanner
echo "[C++] Running process scanner..."
g++ security_diagnostics/hidden_process_guard.cpp -o process_guard
./process_guard >> security_diagnostics/security_alert.log
rm process_guard

# Step 4: C# memory usage checker
echo "[C#] Running memory diagnostics..."
mcs security_diagnostics/diagnose_memory.cs -out:mem_diag.exe
mono mem_diag.exe >> security_diagnostics/security_alert.log
rm mem_diag.exe

# Step 5: Run XML integrity parser
echo "[XML] Verifying integrity hashes..."
python3 security_diagnostics/xml_integrity_parser.py >> security_diagnostics/security_alert.log

echo "[✓] All diagnostics complete. Log saved to: security_diagnostics/security_alert.log"
