ls
cd downloads
ls
cd Lune
ls
cd modules
ls
cd deception
ls
cd fakenuke
ls
python3 injector.py
exit
lanimals
pip install imagemagick
pkg install imagemagick
lanimals
ls
cd LANimals
ls
./setup_termux.sh
python launch.py
ls
python3 lanimals_nexus.py
lanimals vulscan
lanimals tripwire
lanimals dash
lanimals recon
sed -i '1i import os' ~/LANimals/lanimals_nexus.py
lanimals recon
python3 lanimals_nexus.py
# Make sure ~/.local/bin exists and is in your PATH
mkdir -p ~/.local/bin
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
# Symlink each command in bin/ to ~/.local/bin/
for f in ~/LANimals/bin/lanimals_*; do   ln -sf "$f" ~/.local/bin/$(basename "$f"); done
lanimals_roguescan
lanimals_lootlog
lanimals_asciiroll
mkdir -p ~/.local/bin
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
for f in ~/LANimals/bin/lanimals_*; do   ln -sf "$f" ~/.local/bin/$(basename "$f"); done
lanimals_roguescan
lanimals_lootlog
lanimals_asciiroll
lanimal lootlog
ls
oython3 lanimals_nexus.py
python3 lanimals_nexus.py
python3 lanimals-ui.py
python3 lanimals_utils.py
python3 lanimals-ui.py
ls
clear
# Patch all import paths for modules to access lanimals_utils
for f in modules/*.py; do   sed -i '1iimport sys, os\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))' "$f"; done
# Swap /tmp to Termux-safe path
find modules/ -type f -exec sed -i 's|/tmp/|/data/data/com.termux/files/usr/tmp/|g' {} +
# Install ip command if missing
pkg install iproute -y
pkg install iproute2 -y
# Patch all module import paths
for f in modules/*.py; do   sed -i '1iimport sys, os\nsys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))' "$f"; done
# Replace /tmp paths with Termux-safe location
find modules/ -type f -exec sed -i 's|/tmp/|/data/data/com.termux/files/usr/tmp/|g' {} +
# Install the correct ip package
pkg install iproute2 -y
python3 lanimals-ui.py
clear
find modules/ -type f -exec sed -i 's|/data/data/com.termux/files/usr/data/data/com.termux/files/usr/tmp/|/data/data/com.termux/files/usr/tmp/|g' {} +
tmp_path = '/data/data/com.termux/files/usr/tmp/target_net'
os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
with open(tmp_path, 'w') as f:
with open(tmp_path) as f:
os.system("nmap -sP 192.168.1.0/24")
mkdir -p ~/LANimals/loot
# Fix broken double paths
find modules/ -type f -exec sed -i 's|/data/data/com.termux/files/usr/data/data/com.termux/files/usr/tmp/|/data/data/com.termux/files/usr/tmp/|g' {} +
# Create /tmp fallback manually
mkdir -p /data/data/com.termux/files/usr/tmp
# Create loot folder if needed
mkdir -p ~/LANimals/loot
# Remove sudo from scripts (optional)
find modules/ -type f -exec sed -i 's/sudo //g' {} +
python3 lanimals-ui.py
clear
pkg install nmap -y
# Install nmap for network scans
pkg install nmap -y
# Replace ARP logic with ip neigh
echo 'import os\nprint("[✓] ARP Neighbors:")\nos.system("ip neigh")' > modules/arp_recon.py
# Regenerate default target net if not present
echo '192.168.1.0/24' > /data/data/com.termux/files/usr/tmp/target_net
python3 lanimals-ui.py
cat << 'EOF' > modules/arp_recon.py
import os

print("[✓] ARP Neighbors:")
os.system("ip neigh")
EOF

lanimals
ls
ls bin
ls modules
cat << 'EOF' > modules/net_scan.py
import os
import shutil

print("[✓] Network Scan (Non-root fallback)")

if shutil.which("nmap"):
    print("[+] Running Nmap ping sweep...")
    os.system("nmap -sn 192.168.1.0/24")  # Change subnet if needed
else:
    print("[+] Falling back to ping sweep...")
    os.system("for ip in $(seq 1 254); do ping -c 1 -W 1 192.168.1.\$ip | grep 'ttl' & done; wait")
EOF

echo "192.168.1.5 - suspicious MAC - 2025-06-10" >> loot/test_loot.log
cat << 'EOF' > modules/loot_viewer.py
import os

print(r'''
██╗      █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗ ██╗
██║     ██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗██║
██║     ███████║██╔██╗ ██║██║██╔████╔██║███████║██║
██║     ██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║██║
███████╗██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
         LANimals :: Loot Viewer
''')

loot_dir = "loot"
if not os.path.isdir(loot_dir) or not os.listdir(loot_dir):
    print("[!] Loot folder is empty.")
else:
    for f in os.listdir(loot_dir):
        path = os.path.join(loot_dir, f)
        print(f"\n[+] {f}:\n" + "-"*50)
        with open(path) as file:
            print(file.read())
EOF

chmod +x bin/lanimals
ln -s $(pwd)/bin/lanimals $PREFIX/bin/lanimals
cat << 'EOF' > README.md
<p align="center">
  <img src="docs/images/lanimals_banner.png" width="450" alt="LANimals Banner"/>
</p>

<h1 align="center">LANimals</h1>

> **LANimals** is a modular LAN recon and threat mapping suite — stylized terminal ops meet real signal.  
> Passive detection, rogue host tracking, session logging, loot visualization, and more.

---

## Features

- 🧠 Intelligent LAN Sweep
- 🐾 Rogue Host Detection
- 🌐 Passive ARP Monitoring
- 🔎 Threat Grid Visualization
- 📦 Loot Viewer (Artifacts, Logs, Recon Cache)

## Quickstart

```bash
git clone https://github.com/GnomeMan4201/L

cat << 'EOF' > README.md
<p align="center">
  <img src="docs/images/lanimals_banner.png" width="450" alt="LANimals Banner"/>
</p>

<h1 align="center">LANimals</h1>

> **LANimals** is a modular LAN recon and threat mapping suite — stylized terminal ops meet real signal.  
> Passive detection, rogue host tracking, session logging, loot visualization, and more.

---

## Features

- 🧠 Intelligent LAN Sweep
- 🐾 Rogue Host Detection
- 🌐 Passive ARP Monitoring
- 🔎 Threat Grid Visualization
- 📦 Loot Viewer (Artifacts, Logs, Recon Cache)

## Quickstart

```bash
git clone https://github.com/GnomeMan4201/L

cat << 'EOF' > README.md
<p align="center">
  <img src="docs/images/lanimals_banner.png" width="450" alt="LANimals Banner"/>
</p>

<h1 align="center">LANimals</h1>

> **LANimals** is a modular LAN recon and threat mapping suite — stylized terminal ops meet real signal.  
> Passive detection, rogue host tracking, session logging, loot visualization, and more.

---

## Features

- 🧠 Intelligent LAN Sweep
- 🐾 Rogue Host Detection
- 🌐 Passive ARP Monitoring
- 🔎 Threat Grid Visualization
- 📦 Loot Viewer (Artifacts, Logs, Recon Cache)

## Quickstart

```bash
git clone https://github.com/GnomeMan4201/LANimals
cd LANimals
bash install.sh
lanimals
EOF

Just make sure:
- `docs/images/lanimals_banner.png` is your red banner image
- `docs/images/lanimals_demo.png` is a terminal screenshot or the live loop GIF
---
Say the word, and I’ll push you straight into Phase 38: 🎥 terminal GIF/loop builder and `README.md` embed or a live GitHub Pages page.
lanimals
lanimals dash
lanimals recon
lanimals alert
lanimals netmap
lanimals viznet
lanimals hunter
lanimals fortress
lanimals fortress --firewall --fix
lanimals fortress --ssh --fix
lanimals
lanimals threats
lanimals vulnscan
lanimals help
lanimals update
lanimals version
pkg install ncurses-utils -y
pkg update -y
pkg install ncurses-utils -y
mkdir -p docs/images
curl -Lo docs/images/lanimals_banner.png https://via.placeholder.com/450x150.png?text=LANimals+Banner
curl -Lo docs/images/lanimals_demo.png https://via.placeholder.com/800x400.png?text=LANimals+Demo+Preview
cat << 'EOF' > README.md
<p align="center">
  <img src="docs/images/lanimals_banner.png" width="450" alt="LANimals Banner"/>
</p>

<h1 align="center">LANimals</h1>

> **LANimals** is a modular LAN recon and threat mapping suite — stylized terminal ops meet real signal.
> Passive detection, rogue host tracking, session logging, loot visualization, and more.

---

## Features

- 🧠 Intelligent LAN Sweep
- 🐾 Rogue Host Detection
- 🌐 Passive ARP Monitoring
- 🔎 Threat Grid Visualization
- 📦 Loot Viewer (Artifacts, Logs, Recon Cache)

---

## Quickstart

```bash
git clone https://github.com/GnomeMan4201/LANimals
cd LANimals
bash install.sh
lanimals
EOF

pwd
cd ~/LANimals  # or wherever your repo lives
# Clean up pycache and logs
find . -type d -name '__pycache__' -exec rm -rf {} +
rm -f *.log *.tmp .DS_Store .coverage
# Optional: remove `.venv` or test folders if not needed
rm -rf .venv tests __MACOSX
# Confirm clean structure
tree -L 2
# Create ZIP with timestamp
DATE=$(date +%Y%m%d_%H%M%S)
ZIP_NAME="LANimals_DEPLOY_${DATE}.zip"
cd ..
zip -r "$ZIP_NAME" LANimals -x '*.pyc' -x '*.DS_Store' -x '__pycache__/*' -x '.venv/*'
pkg install zip
zip -r "$ZIP_NAME" LANimals -x '*.pyc' -x '*.DS_Store' -x '__pycache__/*' -x '.venv/*'
lanimals
ls
mv LANimals_DEPLOY_20250610_050759.zip downloads
ls
clear
lanimals
lanimals dash
lanimals sysinfo
lanimals recon
lanimals alert
lanimals monitor
lanimals traffic
lanimals netmap
lanimals viznet
lanimals
lanimals threats
lanimals vulnscan
lanimals hunter
lanimals fortress
lanimals --audit
lanimals fortress --audit
clear
lanimals
lanimals fortress --audit
lanimals recon
lanimals netmap
lanimals alert
cd
pwd
lanimals recon
lanimals netmap
lanimals fortress --ssh --fix
lanimals fortress --audit
lanimals sysinfo
ls
cd pwnconsole
ls
cd loot_dump
ls
cd
cd Lune
ls
cd directory
cd
cd directory
ls
cd downloads
lcd
cd
cd downloads
ls
./netdiscovery_v2.sh
./recon_blackice_v3.sh
./setup_bad_banana.sh
npm start
ls
./blackice_recon_deploy.sh
touch ~/.blackice/state/scan_trigger
ls
cd loot
ls
cat targets_indexed.log
cd -
python silent_gate.py
cd bug_bounty_widget
ls
cd backend
ls
python3 recon.py
python recon.py
ls
cd
ls
ls AidRig
