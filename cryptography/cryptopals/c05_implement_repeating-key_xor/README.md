Kỹ thuật: **repeating-key XOR (Vigenère XOR)**

Với bài này, ta được cho một đoạn nhạc (Ice ice baby - Vanilla Ice):

```
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
```

Ý tưởng:
Giả sử ta có:
Plaintext = `P` = `"Burning 'em, if you ain't quick and nimble"` 
Key = `K` = `"ICE"`

Ta sẽ lặp lại key `"ICE"` sao cho nó dài bằng plaintext, rồi XOR từng ký tự tương ứng:

| Plaintext  | B   | u   | r   | n   | i   | n   | g   |
| ---------- | --- | --- | --- | --- | --- | --- | --- |
| Key        | I   | C   | E   | I   | C   | E   | I   |
| XOR result | B^I | u^C | r^E | n^I | i^C | n^E | ... |
|            |     |     |     |     |     |     |     |
=> Tổng quát hóa, có: `C[i] = P[i] ^ K[i % len(K)]`

```
plaintext = input("Plaintext: ")
key = input("Key: ")

# chuyển string -> bytes thì XOR mới hđ
plaintext_bytes = plaintext.encode('utf-8')
key_bytes = key.encode('utf-8')

cipher_bytes = bytearray()

for i in range(len(plaintext_bytes)):
    # lấy 1 byte trong plaintext
    plain_byte = plaintext_bytes[i]
    # lấy 1 byte trong key (% để lặp lại key)
    key_byte = key_bytes[i % len(key_bytes)]
    
    xor_byte = plain_byte ^ key_byte
    
    cipher_bytes.append(xor_byte)

cipher_hex = cipher_bytes.hex()
print(cipher_hex)
```

=>

```
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

