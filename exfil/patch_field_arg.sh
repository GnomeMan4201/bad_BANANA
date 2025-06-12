#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Starting argparse --field injector..."

TARGET_DIR=~/exfil

ARG_BLOCK=$(
cat <<'EOF'
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--field", action="store_true", help="Run in field mode (full exfil + persistence)")
args = parser.parse_args()

if args.field:
    print("[*] Field mode activated. Full deployment authorized.")
EOF
)

for f in "$TARGET_DIR"/*.py; do
    if grep -q "argparse" "$f"; then
        echo "[+] Patching: $(basename "$f")"
        if ! grep -q -- "--field" "$f"; then
            echo "$ARG_BLOCK" >> "$f"
        fi
    fi
done

echo "✅ Patch complete. '--field' support injected where needed."
