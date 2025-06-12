import subprocess, time, os

PROFILE_DIR = "/root/chrome_profile"
COOKIE_URL = "https://httpbin.org/cookies/set?sessionid=987654321"

def start_chromium():
    print("[*] Starting headless Chromium with cookie injection...")
    subprocess.call(f"rm -rf {PROFILE_DIR}/Singleton*", shell=True)

    cmd = (
        f"chromium --headless --disable-gpu --no-sandbox "
        f"--user-data-dir={PROFILE_DIR} "{COOKIE_URL}" &"
    )
    subprocess.call(cmd, shell=True)
    time.sleep(3)
    subprocess.call("pkill chromium", shell=True)

    return f"{PROFILE_DIR}/Default/Cookies"
