import base64

encrypted_message = (
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
)

data_byte = bytes.fromhex(encrypted_message)

max_score = 0
final_message = ""

# every character in ascii values range from 0 to 127 which equals 2 ^ 7
for guessing in range(128):
    character = bytes(guessing)

    decrypt_message = bytearray()

    for byte in data_byte:
        decrypt_message.append(byte ^ guessing)

    plaintext = decrypt_message.decode("ascii")

    score = sum(i.isalpha() for i in plaintext)

    print(f"decrypt: {plaintext}  | {score}")

    if score > max_score:
        final_message = plaintext
        max_score = score


print("---------")
print(f"final answer: {final_message}  | {max_score}")
