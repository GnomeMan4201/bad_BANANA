
#!/usr/bin/env python3
import subprocess
import os
import time

def stage_one_dropper():
    print("[*] Stage 1: Executing dropper...")
    subprocess.Popen(['python3', 'stage_2_loader.py'])
    time.sleep(1)

if __name__ == "__main__":
    stage_one_dropper()
