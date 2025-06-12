#!/bin/bash
set -e

echo "[*] Installing Session Exfil OMEGA CHAIN..."

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

echo "[*] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt || true

# Make launchers executable
chmod +x launcher.py deploy.sh encrypted_loader.py

# Optional: Symlink main launcher for global access
sudo ln -sf $(realpath launcher.py) /usr/local/bin/session-exfil

# Display banner
echo ""
cat BANNER.txt
echo ""

echo "[✓] Install complete! Type 'session-exfil' to start."
