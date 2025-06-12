
#!/usr/bin/env python3
# NO ROOT REQUIRED
# "Choose your bad_BANANA wisely." — Terminal Tactician

import os
import subprocess

BANNER = """\033[1;33m
────────────────────────────────────────────────────────────
🌴  "The bad_BANANA tree is used as an analogy for impermanence,
    highlighting the fleeting nature of virtue's. This is because
    the bad_BANANA tree, while producing fruit, eventually withers."
    — Recut Teachings, Paraphrased
────────────────────────────────────────────────────────────
\033[0m"""

MODULES = [
    "exfil_file_split.py",
    "cookiechain_watcher.py",
    "dropper_generator.py",
    "ngrok_auto_proxy.py",
    "local_vector_map.py",
    "opsec_linter.py",
    "timebomb_launcher.py",
    "filedust.py",
    "coldtrace_killer.py",
    "airdrop_smuggler.py",
    "c2_server.py",
    "memory_only_polymorphic_loader.py",
    "encryptor.py",
    "decrypt_tool.py",
    "otp_bypass_exploit.py",
    "creds_loot.sh",
    "hta_forge.sh",
    "token_dump.sh"
]

def main():
    print(BANNER)
    print("=== bad_BANANA Terminal Launcher ===\n")
    for i, name in enumerate(MODULES):
        print(f"[{i+1:02}] {name}")
    try:
        choice = int(input("\nSelect module number to run: "))
        if 1 <= choice <= len(MODULES):
            target = MODULES[choice - 1]
            print(f"\n[*] Running: {target}\n")
            if target.endswith(".py"):
                subprocess.run(["python3", target])
            else:
                subprocess.run(["bash", target])
        else:
            print("Invalid selection.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
