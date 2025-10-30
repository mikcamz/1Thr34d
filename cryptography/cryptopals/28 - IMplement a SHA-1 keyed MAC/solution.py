import struct
import random

# Hàm xoay trái 32-bit
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(data: bytes) -> bytes:
    h0, h1, h2, h3, h4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
    original_len_in_bits = (8 * len(data)) & 0xffffffffffffffff
    data += b'\x80'
    while (len(data) % 64) != 56:
        data += b'\x00'
    data += struct.pack('>Q', original_len_in_bits)

    for i in range(0, len(data), 64):
        w = [0] * 80
        chunk = data[i:i+64]
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j*4:j*4+4])[0]
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return struct.pack('>IIIII', h0, h1, h2, h3, h4)

def mac_sha1(key: bytes, message: bytes) -> bytes:
    return sha1(key + message)

def verify_mac(key: bytes, message: bytes, mac: bytes) -> bool:
    return mac_sha1(key, message) == mac

key = b'secret123'
message = b'hello bro'
mac = mac_sha1(key, message)

print("MAC gốc:", mac.hex())
print("Verify MAC gốc:", verify_mac(key, message, mac))

tampered = b'hello bro!!'
print("Verify sau khi chỉnh sửa:", verify_mac(key, tampered, mac))

fake_message = b'fake message'

fake_mac = bytes(random.getrandbits(8) for _ in range(20))
print("MAC giả tạo:", fake_mac.hex())
print("Verify MAC giả tạo:", verify_mac(key, fake_message, fake_mac))
