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

import re
from cryptography.fernet import Fernet

# Load encryption key
with open("encryption_key.key", "rb") as keyfile:
    key = keyfile.read()
cipher = Fernet(key)

# Define regex patterns for common token formats
TOKEN_PATTERNS = [
    r'(?i)bearer\s+([a-zA-Z0-9\-_]+)',  # Bearer tokens
    r'eyJ[a-zA-Z0-9\-_]+\.eyJ[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+',  # JWT Tokens
    r'ghp_[a-zA-Z0-9]{36}',  # GitHub Personal Access Tokens
    r'ya29\.[0-9A-Za-z\-_]+',  # Google OAuth Tokens
    r'AKIA[0-9A-Z]{16}',  # AWS Access Key
    r'AIza[0-9A-Za-z\-_]{35}',  # Google API Key
]

# Read token file
with open("realtime_leaked_keys.log", "r") as file:
    lines = file.readlines()

valid_tokens = []
invalid_tokens = []

# Scan each line
for line in lines:
    token_found = None
    for pattern in TOKEN_PATTERNS:
        match = re.search(pattern, line)
        if match:
            token_found = match.group(0)
            break
    
    if token_found:
        print(f"[✅] Valid Token Found: {token_found}")
        valid_tokens.append(token_found)
    else:
        print(f"[❌] Invalid Token: {line.strip()}")
        invalid_tokens.append(line.strip())

# Encrypt valid tokens
with open("secure_tokens.enc", "wb") as enc_file:
    for token in valid_tokens:
        encrypted_token = cipher.encrypt(token.encode())
        enc_file.write(encrypted_token + b"\n")

print(f"\n🔒 Encrypted {len(valid_tokens)} valid tokens.")
print(f"⚠️ Ignored {len(invalid_tokens)} non-token entries.")

