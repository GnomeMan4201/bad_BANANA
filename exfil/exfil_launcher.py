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
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

MODULES = {
    "1": ("DNS Exfiltration", "core/exfil_dns.py"),
    "2": ("HTTPS Exfiltration", "core/exfil_https.py"),
    "3": ("WebSocket Exfiltration", "core/exfil_ws.py"),
    "4": ("Autopilot Exfil", "exfil_autopilot.py"),
    "5": ("Ngrok Exfil", "exfil_ngrok.py"),
    "6": ("Sync Exfil", "exfil_sync.sh"),
    "7": ("Listener Server", "exfil_listener.py"),
    "8": ("Live Token Exploit", "live_token_exploit.sh"),
    "9": ("JS Dropper", "modules/js_dropper.py"),
    "10": ("Encrypted Image Stego Exfil", "modules/image_stego_exfil.py"),
    "11": ("Web Archive Upload Exfil", "modules/archive_upload_exfil.py"),
}

def banner():
    console.print(Panel.fit("[bold red]SESSION EXFIL SUITE[/bold red]\n[white]by NMAPKin[/white]", border_style="bright_red"))

def show_menu():
    table = Table(title="Exfiltration Modules", show_lines=True)
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Module", style="magenta")

    for key, (desc, _) in MODULES.items():
        table.add_row(key, desc)

    console.print(table)

def run_module(path):
    console.print(f"[green]Launching:[/green] {path}")
    if path.endswith(".py"):
        os.system(f"python3 {path}")
    elif path.endswith(".sh"):
        os.system(f"bash {path}")
    else:
        console.print(f"[red]Unsupported module type:[/red] {path}")

def main():
    banner()
    while True:
        show_menu()
        choice = Prompt.ask("[bold yellow]Select module[/bold yellow] (or Q to quit)")
        if choice.lower() == 'q':
            console.print("[bold red]Exiting...[/bold red]")
            break
        if choice in MODULES:
            _, path = MODULES[choice]
            run_module(path)
        else:
            console.print("[red]Invalid selection.[/red]")

if __name__ == "__main__":
    main()
