from base64 import b64decode

def hamming_distance(a, b):
    return sum(bin(b1 ^ b2).count("1") for b1, b2 in zip(a, b))

# Đọc file mã hoá (Challenge 6)
with open("6.txt") as file:
    ciphertext = b64decode(file.read())

# Đánh giá “điểm” cho mỗi keysize khả thi
def score_vigenere_key_size(keysize, ciphertext):
    block_size = 2 * keysize
    measure_block = len(ciphertext) // block_size - 1
    score = 0

    for i in range(measure_block):
        s = block_size
        k = keysize
        b1 = slice(i * s, i * s + k)
        b2 = slice(i * s + k, i * s + 2 * k)
        score += hamming_distance(ciphertext[b1], ciphertext[b2])

    score /= measure_block
    score /= keysize

    return score

# Tìm ra keysize phù hợp nhất
def find_suitable_key_size(ciphertext, min_size=2, max_size=40):
    scores = []
    for keysize in range(min_size, max_size + 1):
        score = score_vigenere_key_size(keysize, ciphertext)
        scores.append((keysize, score))
    scores.sort(key=lambda x: x[1]) # sắp xếp theo điểm số
    return scores[:3]  # trả về 3 keysize có điểm thấp nhất

# Dùng lại logic brute-force từ Challenge 3
def attack_single_byte_xor(cipher):
    best = None
    best_key = None
    best_text = None

    for key in range(256):
        plain_bytes = bytes([b ^ key for b in cipher])
        try:
            plain_text = plain_bytes.decode('ascii')
        except UnicodeDecodeError:
            continue

        # tính điểm dựa trên tần suất ký tự tiếng Anh phổ biến
        score = sum(c in b"ETAOIN SHRDLUetaoinshrdlu " for c in plain_bytes)

        if not best or score > best:
            best = score
            best_key = key
            best_text = plain_bytes

    return {
        "key": bytes([best_key]),
        "message": best_text,
        "score": best
    }

# Hàm chính: Giải Repeating-key XOR
def main(ciphertext):
    # lấy keysize có điểm thấp nhất
    keysize = find_suitable_key_size(ciphertext)[0][0]
    print(f"Best key size guess: {keysize}")

    key = b""
    blocks = []

    # tách ciphertext thành từng block theo vị trí key
    for i in range(keysize):
        block = bytes(ciphertext[j] for j in range(i, len(ciphertext), keysize))
        result = attack_single_byte_xor(block)
        key += result["key"]
        blocks.append(result["message"])

    # ghép lại plaintext theo đúng thứ tự byte
    plaintext = b""
    for i in range(max(len(b) for b in blocks)):
        for b in blocks:
            if i < len(b):
                plaintext += bytes([b[i]])

    print("Key found:", key.decode(errors="ignore"))
    print("Plaintext:\n")
    print(plaintext.decode(errors="ignore"))

main(ciphertext)