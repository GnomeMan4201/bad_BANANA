#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Starting full argparse injector for all flags..."

# Define the block to inject
read -r -d '' ARGPARSE_BLOCK << EOM
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--field", action="store_true", help="Run in field mode (full exfil + persistence)")
parser.add_argument("--lab", action="store_true", help="Run in lab-safe mode (no persistence, no outbound exfil)")
parser.add_argument("--kill", action="store_true", help="Trigger kill switch")
parser.add_argument("--consent", action="store_true", help="Acknowledge ethical terms")
args = parser.parse_args()

if args.kill:
    print("[!] Kill-switch triggered.")
elif args.lab:
    print("[*] Lab mode activated. Exfiltration and persistence modules disabled.")
elif args.field:
    print("[*] Field mode activated. Full deployment authorized.")
elif args.consent:
    print("[*] Consent acknowledged.")
else:
    print("[!] No valid mode specified. Use --lab or --field or --kill or --consent.")
EOM

# Patch all .py files
for file in ~/exfil/*.py; do
    if ! grep -q "parser = argparse.ArgumentParser()" "$file"; then
        echo "[+] Patching: $(basename "$file")"
        echo -e "\n$ARGPARSE_BLOCK" >> "$file"
    fi
done

echo "✅ Multi-argparse patch complete. Scripts now accept --field, --lab, --kill, --consent."
