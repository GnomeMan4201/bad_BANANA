import os
from datetime import datetime

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

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

KEY = b"ThisIsA32ByteKeyForAES256Crypto!!"

def encrypt_payload(data: bytes) -> str:
    nonce = get_random_bytes(12)
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return base64.urlsafe_b64encode(nonce + tag + ciphertext).decode()

def decrypt_payload(encoded: str) -> bytes:
    raw = base64.urlsafe_b64decode(encoded)
    nonce, tag, ciphertext = raw[:12], raw[12:28], raw[28:]
    cipher = AES.new(KEY, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
