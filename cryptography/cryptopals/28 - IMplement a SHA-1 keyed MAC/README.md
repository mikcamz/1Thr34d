Ý tưởng đề: 
Mục tiêu viết hàm tạo MAC cho một message bằng secret-prefix MAC theo công thức:

`MAC = SHA1( key || mesage)`

với key là bí mật mà chỉ người ký (host) (server) biết. Sau đó viết hàm kiểm tra MAC và chứng minh rằng nếu không biết key thì:
- Không thể sửa mesage mà giữ MAC hợp lệ
- Không thể tạo MAC mới cho message mới (không có key).

Khái niệm cần biết:
"MAC" là gì?
MAC (Message Authentication Code) là một đoạn mã ngắn được tạo ra từ:
- một message 
- một secret key.
Mục đích là:
- Xác thực tính toàn vẹn (integrity) của message
- Xác minh nguồn gốc (authenticity), chỉ ai biết secret key mới có thể tạo ra MAC hợp lệ.
Nếu thông điệp bị chỉnh sửa hoặc người không biết khóa cố gắng tạo MAC mới thì kiểm tra sẽ thấy bại.

Secret-prefix MAC: 
Cách dựng: `MAC = SHA1( key || message )`
Trong đó: 
- `||` là phép nối chuỗi
- Ghép secret key trước message rồi hash (băm) toàn bộ.

Ví dụ:

```
import hashlib

def mac_sha1(key: bytes, message: bytes) -> bytes:
    return hashlib.sha1(key + message).digest()

def verify_mac(key: bytes, message: bytes, mac: bytes) -> bool:
    return mac_sha1(key, message) == mac

key = b'secret123'
message = b'hello bro'
mac = mac_sha1(key, message)

print("MAC:", mac.hex())
print("Verify:", verify_mac(key, message, mac))

tampered = b'hello bro!!'
print("Verify after tamper:", verify_mac(key, tampered, mac))

```

Kết quả:

```
MAC: 1091ff37233b85dc9deb77c97f14330d5cefd143
Verify: True
Verify after tamper: False
```

=> Không thể giả mạo hoặc thay đổi message mà vẫn giữ MAC hợp lệ, nếu không biết key.

Nhưng vẫn có điểm yếu:
SHA1 (và các hàm băm tương tự như MD5, SHA256,...) dễ bị `length extension attack` nếu dùng kiểu nối `key || message`.
Một attacker có thể mở rộng message hợp lệ mà không cần biết key, chỉ bằng cách lợi dụng tính chất nội bộ của hàm băm.

Ý tưởng:
1. Hàm `sha1(data)`
- Khởi tạo: Bắt đầu với 5 giá trị hash (hằng số) ban đầu `h0` đến `h4`.
- Đệm (Padding): Xử lý dữ liệu đầu vào (`data`) để đảm bảo độ dài của nó là bội số của 512 bit (64 bytes).
    1. Thêm bit `1` (tức là byte `b'\x80'`).
    2. Thêm các bit `0` (các byte `b'\x00'`) cho đến khi độ dài dữ liệu là 56 bytes (mod 64).
    3. Thêm 8 byte cuối cùng (64 bit) biểu thị độ dài _ban đầu_ của dữ liệu.
- Xử lý theo khối (Chunk Processing):
    - Lặp qua từng khối 64 byte của dữ liệu đã đệm.
    - Tạo ra một message schedule `w` gồm 80 từ 32-bit từ khối 64 byte đó.
    - Thực hiện 80 vòng lặp nén. Trong mỗi vòng lặp:
        - Sử dụng các hàm logic, hằng số `k`, và phép xoay bit (`left_rotate`) khác nhau tùy thuộc vào vòng lặp (vòng 0-19, 20-39, 40-59, 60-79).
        - Cập nhật 5 biến `a, b, c, d, e`.
    - Cộng kết quả nén của khối này vào các giá trị hash `h0` đến `h4`.
=> Nối 5 giá trị hash cuối cùng lại để tạo ra một chuỗi 20-byte (160-bit) duy nhất, đó chính là "dấu vân tay" SHA-1 của dữ liệu.

Hàm `mac_sha1(key, message)`
Đây là hàm tạo MAC:
- Nối `secret key` bí mật vào trước `message`
- Hash toàn bộ chuỗi kết quả đó bằng hàm `sha1`.
=> Kết quả 20-byte chính là cái MAC.

Main
Minh họa ý tưởng của MAC:
- Tạo MAC gốc: `MAC = SHA1( key || message )`
- Không thể sửa mesage mà giữ MAC hợp lệ:
    - Tạo một `tampered` 
    - Thử xác thực tin nhắn `tampered` này với cái `MAC` gốc 
- Không thể tạo MAC mới cho message mới (không có key):
    - Tạo một `fake_message` và một `fake_mac` (20 byte ngẫu nhiên).
    - Thử xác thực `fake_message` với `fake_mac`.

Code:

```
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

# Không thể sửa mesage mà giữ MAC hợp lệ
tampered = b'hello bro!!'
print("Verify sau khi chỉnh sửa:", verify_mac(key, tampered, mac))

#Không thể tạo MAC mới cho message mới (không có key)
fake_message = b'fake message'
fake_mac = bytes(random.getrandbits(8) for _ in range(20))

print("MAC giả tạo:", fake_mac.hex())
print("Verify MAC giả tạo:", verify_mac(key, fake_message, fake_mac))
```

=>
```
MAC gốc: 1091ff37233b85dc9deb77c97f14330d5cefd143
Verify MAC gốc: True
Verify sau khi chỉnh sửa: False
MAC giả tạo: 36c664c23374e8f9c40d51ce9e3bf8093abec500
Verify MAC giả tạo: False
```
