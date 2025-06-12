
# Session Exfil OMEGA — Chromium Cookie Edition

This project demonstrates real Chromium cookie grabbing *on a non-rooted Android* device using Termux + Debian proot-distro + Shizuku.

---

## 🔥 What It Does

- Boots a Linux-like env on Android via Termux (no root)
- Launches Chromium in headless mode with fake session cookies
- Extracts cookies from the SQLite DB (real file: `Cookies`)
- Outputs them in base64

---

## 🚀 Setup Instructions

1. **Install Termux** and run:
   ```bash
   pkg install proot-distro
   proot-distro install debian
   proot-distro login debian
   ```

2. **Install Chromium** inside Debian:
   ```bash
   apt update && apt install chromium
   ```

3. **Run the included script**:
   ```bash
   bash scripts/launch_chromium_cookie_setter.sh
   python3 plugins/grab_cookies.py
   ```

---

## ⚠️ Legal Notice

This project is for **educational and research** purposes only.  
Do **not** use it to access, steal, or manipulate cookies or accounts you do not own.  
Unauthorized use can be **illegal** and is strictly discouraged.

You're responsible for how you use this tool.

---

