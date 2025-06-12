#!/data/data/com.termux/files/usr/bin/bash

cd ~/exfil || { echo "❌ Failed to enter exfil directory"; exit 1; }

# Create ZIP archive of everything inside ~/exfil
zip -r ~/exfil_backup.zip . -x "*.pyc" -x "__pycache__/*"

echo "✅ Backup complete: ~/exfil_backup.zip"
