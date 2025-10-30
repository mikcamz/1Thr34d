Bài cho file `7.txt` chứa ciphertext được encode bằng base64, ciphertext đó đã được mã hóa bằng AES-128 ở chế độ ECB với khóa `"YELLOW SUBMARINE"` (16 bytes).

Khái niệm cần lưu ý:
AES (Advanced Encryption Standard) là thuật toán mã hóa đối xứng.
	-> `đối xứng` là cùng 1 key có thể encode và decode.
AES-128 là việc AES có thể dùng khóa dài 128, 192 hoặc 256 bit.
	-> `128 bit = 16 byte = 16 ký tự ASCII (1 char = 1 byte)`
	Ví dụ: `YELLOW SUBMARINE` = 16 ký tự = 16 byte => key 128-bit hợp lệ.
=> AES không mã hóa toàn bộ văn bản một lượt mà chia thành nhiều khối nhỏ (mỗi khối 16 byte).
ECB (Electronic Codebook) là chế độ hoạt động đơn giản nhất:
	- Mỗi khối plaintext được mã hóa riêng biệt bằng cùng 1 key.
	- Không có "liên kết" giữa các khối.
	Nghĩa là:
	
```
Plaintext block 1 → Encrypt → Ciphertext block 1
Plaintext block 2 → Encrypt → Ciphertext block 2
...
```

Nhưng nhược điểm thì ối dồi ôi:
`Nếu 2 khối plaintext giống hệt nhau <=> ciphertext giống nhau`

Giả sử:
```
plaintext = "HELLOHELLOHELLO"
key = "YELLOW SUBMARINE"
```

AES chia ra:
```
HELLOHELLOHELLO
↓ (chia block)
[HELLOHELLOHELLO] (3 block 16 bytes)
↓
Mã hoá từng block riêng rẽ bằng cùng key
↓
Ciphertext
```

=> ECB dễ bị phân tích mẫu (pattern).

Ý tưởng:
Và ta phải decode base64 -> bytes -> giải AES-128-ECB bằng key trên -> xuất plaintext.

Code:

```
from base64 import b64decode
from Crypto.Cipher import AES

# đọc file và decode base64 -> bytes
with open("7.txt") as f:
    ciphertext = b64decode(f.read())

key = b"YELLOW SUBMARINE"

# tạo một đối tượng AES với khóa trên, ở chế độ ECB, đây là đối tượng sẽ thực hiện phép giải mã
cipher = AES.new(key, AES.MODE_ECB)

# giải mã ciphertext (bytes) -> trả về plaintext dạng bytes
plaintext = cipher.decrypt(ciphertext)

# chuyển `bytes` -> chuỗi UTF-8 để in
print(plaintext.decode('utf-8'))
```


Trong wsl2 bị lỗi `ModuleNotFoundError: No module named 'Crypto'`
nên mình tạo venv (virtual environment):

```
python3 -m venv venv

pip install pycryptodome
```

