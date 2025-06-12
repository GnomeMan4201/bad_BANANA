#!/bin/bash
echo "[*] Installing Session Exfil..."
pip install pycryptodome >/dev/null 2>&1
chmod +x main.py
ln -sf $(realpath main.py) $PREFIX/bin/session_exfil
echo "[✓] Installed. Run: session_exfil"
