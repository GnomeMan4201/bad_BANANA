#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[*] Installing Session Exfil OMEGA CHAIN (No-Crypto Fork)..."

python3 -m venv .venv
source .venv/bin/activate

echo "[*] Installing safe dependencies..."
pip install --upgrade pip
pip install requests dnspython paho-mqtt

echo "[*] Creating symlinks..."
chmod +x omega_operator_console.py exfil_launcher.py
ln -sf $(realpath omega_operator_console.py) $PREFIX/bin/omega-operator
ln -sf $(realpath exfil_launcher.py) $PREFIX/bin/omega-launcher

echo "[✓] Install complete!"
echo "    ➤ Use: omega-operator"
