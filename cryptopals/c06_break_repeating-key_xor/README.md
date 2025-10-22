Đề cho ta file base64 đã bị mã hoá bằng repeating-key xor (vigenere). cần tìm key và giải plaintext.

Ý tưởng:
- Đoán độ dài key (keysize) bằng cách so sánh hamming distance giữa các khối liên tiếp.
- Với mỗi candidate keysize (thử 2..40), lấy nhiều cặp block cùng độ dài = keysize, tính hamming distance giữa từng cặp, chuẩn hoá bằng keysize rồi lấy trung bình. Keysize có normalized distance nhỏ nhất là ứng viên tốt.
- Khi biết keysize: chuyển đổi ciphertext, tức lấy các byte có cùng offset modulo keysize thành 1 block, mỗi block tương ứng với single-byte xor (chỉ xor với 1 byte key).
- Dùng brute-force 256 giá trị cho mỗi transposed block (chính xác như `3`) rồi chấm điểm bằng metric tiếng anh (ở đây dùng tần suất chữ thường phổ biến). byte có score cao nhất là byte key tương ứng.
- Ghép các byte key lại, xor lặp key với toàn bộ ciphertext để ra plaintext.

Công thức đảo `XOR`:
- nếu `ciphertext[i] = plaintext[i] ^ key[i % keysize]`
- thì `plaintext[i] = ciphertext[i] ^ key[i % keysize]`

Code sau:

```
from base64 import b64decode

def hamming_distance(a, b):
    return sum(bin(b1 ^ b2).count("1") for b1, b2 in zip(a, b))

# Đọc file mã hoá (Challenge 6)
with open("6.txt") as f:
    ciphertext = b64decode(f.read())

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
```

=>
```
Best key size guess: 29
Key found: Terminator X: Bring the noise
Plaintext:

I'm back and I'm ringin' the bell
A rockin' on the mike while the fly girls yell
In ecstasy in the back of me
Well that's my DJ Deshay cuttin' all them Z's
Hittin' hard and the girlies goin' crazy
Vanilla's on the mike, man I'm not lazy.

I'm lettin' my drug kick in
It controls my mouth and I begin
To just let it flow, let my concepts go
My posse's to the side yellin', Go Vanilla Go!

Smooth 'cause that's the way I will be
And if you don't give a damn, then
Why you starin' at me
So get off 'cause I control the stage
There's no dissin' allowed
I'm in my own phase
The girlies sa y they love me and that is ok
And I can dance better than any kid n' play

Stage 2 -- Yea the one ya' wanna listen to
It's off my head so let the beat play through
So I can funk it up and make it sound good
1-2-3 Yo -- Knock on some wood
For good luck, I like my rhymes atrocious
Supercalafragilisticexpialidocious
I'm an effect and that you can bet
I can take a fly girl and make her wet.

I'm like Samson -- Samson to Delilah
There's no denyin', You can try to hang
But you'll keep tryin' to get my style
Over and over, practice makes perfect
But not if you're a loafer.

You'll get nowhere, no place, no time, no girls
Soon -- Oh my God, homebody, you probably eat
Spaghetti with a spoon! Come on and say it!

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino
Intoxicating so you stagger like a wino
So punks stop trying and girl stop cryin'
Vanilla Ice is sellin' and you people are buyin'
'Cause why the freaks are jockin' like Crazy Glue
Movin' and groovin' trying to sing along
All through the ghetto groovin' this here song
Now you're amazed by the VIP posse.

Steppin' so hard like a German Nazi
Startled by the bases hittin' ground
There's no trippin' on mine, I'm just gettin' down
Sparkamatic, I'm hangin' tight like a fanatic
You trapped me once and I thought that
You might have it
So step down and lend me your ear
'89 in my time! You, '90 is my year.

You're weakenin' fast, YO! and I can tell it
Your body's gettin' hot, so, so I can smell it
So don't be mad and don't be sad
'Cause the lyrics belong to ICE, You can call me Dad
You're pitchin' a fit, so step back and endure
Let the witch doctor, Ice, do the dance to cure
So come up close and don't be square
You wanna battle me -- Anytime, anywhere

You thought that I was weak, Boy, you're dead wrong
So come on, everybody and sing this song

Say -- Play that funky music Say, go white boy, go white boy go
play that funky music Go white boy, go white boy, go
Lay down and boogie and play that funky music till you die.

Play that funky music Come on, Come on, let me hear
Play that funky music white boy you say it, say it
Play that funky music A little louder now
Play that funky music, white boy Come on, Come on, Come on
Play that funky music
```
