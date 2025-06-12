#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Scanning and fixing argparse --field conflicts..."

cd ~/exfil || exit 1

for file in *.py; do
    if grep -q 'add_argument("--field"' "$file"; then
        echo "[*] Removing existing --field from $file"
        # Remove all lines that add --field
        sed -i '/add_argument("--field"/d' "$file"
    fi

    # Ensure the parser exists and add --field argument if missing
    if grep -q 'ArgumentParser' "$file"; then
        if ! grep -q 'add_argument("--field"' "$file"; then
            echo "[*] Injecting cleaned --field into $file"
            sed -i '/ArgumentParser/a \    parser.add_argument("--field", action="store_true", help="Field mode (exfil+persistence)")' "$file"
        fi
    fi
done

echo "✅ Field argument conflict patch complete."
