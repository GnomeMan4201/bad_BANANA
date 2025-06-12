#!/data/data/com.termux/files/usr/bin/bash
echo "[!] Self-destruct sequence triggered..."
rm -rf ~/exfil/.logs/*
rm -rf ~/exfil/__pycache__/*
echo "[*] Wipe complete. Terminating session."
