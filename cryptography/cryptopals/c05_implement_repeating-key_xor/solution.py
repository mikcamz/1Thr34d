plaintext = input("Plaintext: ")
key = input("Key: ")

plaintext_bytes = plaintext.encode('utf-8')
key_bytes = key.encode('utf-8')

cipher_bytes = bytearray()

for i in range(len(plaintext_bytes)):

    plain_byte = plaintext_bytes[i]

    key_byte = key_bytes[i % len(key_bytes)]

    xor_byte = plain_byte ^ key_byte

    cipher_bytes.append(xor_byte)

cipher_hex = cipher_bytes.hex()
print("Cipher (hex):")
print(cipher_hex)

'''
decoded_bytes = bytearray()
for i in range(len(cipher_bytes)):
    decoded_byte = cipher_bytes[i] ^ key_bytes[i % len(key_bytes)]
    decoded_bytes.append(decoded_byte)

print("\nDecrypted back to plaintext:")
print(decoded_bytes.decode('utf-8'))
'''