#!/data/data/com.termux/files/usr/bin/bash
echo "[*] Fixing indentation errors and cleaning --field arg insertions..."

for f in *.py; do
    if grep -q "add_argument(\"--field\"" "$f"; then
        echo "[*] Cleaning $f"
        sed -i '/--field/d' "$f"
        sed -i '/argparse.ArgumentParser()/a\    parser.add_argument("--field", action="store_true", help="Field mode (exfil+persistence)")' "$f"
    fi
done

echo "[+] Indentation and argparse patching complete."
