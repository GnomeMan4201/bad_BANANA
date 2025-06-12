#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Ensuring 'import os' and 'from datetime import datetime' are present..."

TARGET_DIR=~/exfil
LOG_IMPORTS="import os\nfrom datetime import datetime"

for file in $(find $TARGET_DIR -maxdepth 1 -name "*.py"); do
    if ! grep -q "import os" "$file"; then
        sed -i "1s;^;$LOG_IMPORTS\n;" "$file"
        echo "[+] Injected missing imports: $(basename "$file")"
    fi
done

echo "✅ Import fix complete."
