
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
