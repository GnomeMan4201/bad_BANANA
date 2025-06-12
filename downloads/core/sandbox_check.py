import os

def is_sandbox():
    return any(s in os.getenv("USERNAME", "").lower() for s in ["sandbox", "malware", "virus"]) or os.path.exists("/.dockerenv")