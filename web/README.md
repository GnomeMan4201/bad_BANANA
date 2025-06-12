
<p align="center">
  <img src="https://raw.githubusercontent.com/GnomeMan4201/bad_BANANA/main/assets/logo.png" alt="bad_BANANA logo" width="300"/>
</p>

# bad_BANANA

A field-ready, no-root offensive toolkit for Android (Termux) + Debian.

---

## 🍌 What It Does

- Boots a Linux-like environment on Android via Termux (no root)
- Launches Chromium in headless mode with fake session cookies
- Extracts cookies from the SQLite DB (real file: `Cookies`)
- Outputs them in base64

---

## 🛠️ Setup Instructions

### 1. Install Termux and run:

```bash
pkg install proot-distro
proot-distro install debian
proot-distro login debian
```

### 2. Install Chromium inside Debian:

```bash
apt update && apt install chromium
```

### 3. Run the included script:

```bash
bash scripts/launch_chromium_cookie_setter.sh
python3 plugins/grab_cookies.py
```

---

## ⚠️ Legal Notice

This project is for **educational and research** purposes only.  
Do **not** use it to access, steal, or manipulate cookies or accounts you do not own.

**Unauthorized use can be illegal** and is strictly discouraged.  
You are responsible for how you use this tool.

---

© 2025 GnomeMan4201 / bad_BANANA Project
