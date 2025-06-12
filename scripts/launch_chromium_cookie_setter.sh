
#!/bin/bash
echo "[*] Launching Chromium to set test cookie..."
rm -rf ~/chrome_profile/Singleton*
chromium --headless --disable-gpu --no-sandbox \
  --user-data-dir=~/chrome_profile \
  "https://httpbin.org/cookies/set?sessionid=987654321"
