import base64, sys
def obfuscate(path):
    with open(path, 'r') as f:
        code = f.read()
    encoded = base64.b64encode(code.encode()).decode()
    wrapper = f"import base64;exec(base64.b64decode('{encoded}'))"
    with open(path.replace('.py', '_obf.py'), 'w') as f:
        f.write(wrapper)

if __name__ == "__main__":
    obfuscate(sys.argv[1])
