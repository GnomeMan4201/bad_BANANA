def xor(data, key=0x5A):
    return bytes([b ^ key for b in data])