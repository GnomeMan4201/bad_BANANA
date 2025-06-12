
import sqlite3
import os
import base64
import json
from http.cookies import SimpleCookie

def grab_chromium_cookies(cookie_file_path):
    if not os.path.exists(cookie_file_path):
        print("[!] Cookie DB not found.")
        return
    try:
        conn = sqlite3.connect(cookie_file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, encrypted_value, expires_utc FROM cookies")
        for host, name, value, expires in cursor.fetchall():
            print(f"\n[+] Host: {host}")
            print(f"    Name: {name}")
            print(f"    Value (base64): {base64.b64encode(value).decode()}")
            print(f"    Expires: {expires} (UTC format: 1970-01-01 00:00:00)")
        conn.close()
    except Exception as e:
        print(f"[!] Error reading cookies: {e}")

if __name__ == "__main__":
    path = os.path.expanduser("~/chrome_profile/Default/Cookies")
    grab_chromium_cookies(path)
