#!/data/data/com.termux/files/usr/bin/python3

from flask import Flask, request
import os

app = Flask(__name__)
loot_log = os.path.expanduser("~/pwnconsole/loot/exfil.log")

@app.route("/exfil", methods=["POST"])
def exfil():
    data = request.form.get("exfil")
    if data:
        with open(loot_log, "a") as f:
            f.write(data + "\n")
        print(f"[+] Exfil received: {data}")
        return "Exfil received", 200
    return "No data", 400

if __name__ == "__main__":
    print("[*] Exfil listener live on http://127.0.0.1:8080/exfil")
    app.run(host="127.0.0.1", port=8080)
