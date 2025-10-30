from base64 import b64decode
from Crypto.Cipher import AES

with open("7.txt") as f:
    ciphertext = b64decode(f.read())

key = b"YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode('utf-8'))