#!/data/data/com.termux/files/usr/bin/bash

# Make sure logs directory exists
mkdir -p ~/exfil/.logs

# Use HOME instead of /tmp for compatibility with Termux
LOG_SNIPPET_FILE="$HOME/.log_snippet.py"

# Write the logging function
cat > "$LOG_SNIPPET_FILE" << 'EOF'
import os
from datetime import datetime

LOG_PATH = os.path.expanduser("~/exfil/.logs/exfil.log")

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"[{timestamp}] {event}\n")
EOF

# Inject into all top-level Python scripts in ~/exfil
TARGET_FILES=$(find ~/exfil -maxdepth 1 -name "*.py")

for file in $TARGET_FILES; do
    # Inject the logging function if not already present
    if ! grep -q "def log_event" "$file"; then
        cat "$LOG_SNIPPET_FILE" "$file" > "${file}.patched"
        mv "${file}.patched" "$file"
    fi

    # Add log_event call after each print statement
    sed -i -E 's/print([^)]+)/print(\1); log_event(\1)/g' "$file"
done

# Cleanup
rm -f "$LOG_SNIPPET_FILE"

echo "[+] Logging successfully injected into all Python scripts. ✅"
