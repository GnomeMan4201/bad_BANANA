#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Starting full auto-patch for Exfil Suite..."

EXFIL_DIR=~/exfil
MODULE_DIR="$EXFIL_DIR/modules"
CORE_DIR="$EXFIL_DIR/core"
LOG_IMPORTS="import os\nfrom datetime import datetime"

# Step 1: Inject argparse flags into every .py file
echo "[*] Injecting argparse flags..."

for file in "$EXFIL_DIR"/*.py; do
    if grep -q 'argparse' "$file"; then
        sed -i '/parser = argparse.ArgumentParser()/a \
parser.add_argument("--lab", action="store_true")\n\
parser.add_argument("--field", action="store_true")\n\
parser.add_argument("--consent", action="store_true")\n\
parser.add_argument("--kill", action="store_true")' "$file"
    fi
done
echo "✅ Argparse injection complete."

# Step 2: Ensure 'import os' and 'from datetime' are present
echo "[*] Checking imports..."

for file in "$EXFIL_DIR"/*.py; do
    grep -q 'import os' "$file" || sed -i "1i $LOG_IMPORTS" "$file"
done
echo "✅ Import fixes complete."

# Step 3: Patch file paths if scripts reference missing paths
echo "[*] Patching module/core paths in operator_menu.sh..."

sed -i 's#core/#./#g' "$EXFIL_DIR/operator_menu.sh"
sed -i 's#modules/#./#g' "$EXFIL_DIR/operator_menu.sh"

echo "✅ Path fixes complete."

# Step 4: Make everything executable
echo "[*] Applying chmod +x to all shell scripts..."
chmod +x "$EXFIL_DIR"/*.sh

echo "✅ Auto-patch complete. Run with:"
echo "$EXFIL_DIR/operator_menu.sh"
