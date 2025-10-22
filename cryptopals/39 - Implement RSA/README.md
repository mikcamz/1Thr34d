Bài 39 muốn ta tự cài đặt RSA (tất nhiên không dùng thư viện có sẵn), theo từng bước thủ công để hiểu bản chất toán học của RSA.

Theo tác giả thì:
Cần viết hai hàm toán học cơ bản 'annoying':
- EGCD (Extended Euclidean Algorithm, thuật toán Euclid mở rộng)
	-> dùng để tìm `x, y` sao cho `a*x + b*y = gcd(a, b)`
- invmod(a, m): tìm nghịch đảo modular của `a` theo modulo `m`
	Tức là tìm `x` sao cho: `(a * x) % m == 1`
	Ví dụ: `invmod(17, 3120) = 2753` vì `17 * 2753 % 3120 == 1`
Chọn 2 số ngto ngẫu nhiên p và q và cho e.
Tính các giá trị `N`, `phi`, `d`.
Sinh khóa `public & private`
Viết hàm mã hóa và giải mã.

Code sau:

```
def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, g = egcd(b, a % b)

        return (y, x - (a // b) * y, g)

def invmod(a, m):
    x, y, g = egcd(a, m)

    if g != 1:
        raise ValueError("No modular inverse")

    return (x % m + m) % m

p, q = 1000003, 1000037 # chọn sao cho gcd(e, phi) = 1
N = p * q
phi = (p - 1) * (q - 1) 

e = 65537  # || e = 17 || e = 3
d = invmod(e, phi)

print(f"Public key: (N = {N}, e = {e})")
print(f"Private key: d = {d}")


# test 1 - với m = 42
m = 42
c = pow(m, e, N)
m_decrypted = pow(c, d, N)

print("\n# Test 1:")
print(f"Plaintext: {m}")
print(f"Ciphertext: {c}")
print(f"Decrypted: {m_decrypted}")
  

# test 2 - với 1 chuỗi bất kỳ
text = input("\nNhập chuỗi cần mã hóa: ")

m_int = int.from_bytes(text.encode('utf-8'), byteorder='big')

# kiểm tra 0 <= m-int < N (điều kiện RSA)
if m_int >= N:
    raise ValueError("Chuỗi dài hơn N, không thể mã hóa bằng RSA với khóa hiện tại (dùng p, q lớn hơn)")
else:
    c = pow(m_int, e, N)
    m_decrypted_int = pow(c, d, N)

    decrypted_text = m_decrypted_int.to_bytes((m_decrypted_int.bit_length() + 7) // 8, 'big').decode('utf-8')

    print("\n# Test 2:")
    print(f"Plaintext: {text}")
    print(f"Ciphertext: {c}")
    print(f"Decrypted: {decrypted_text}")
```

Trong đó:
Endian (hay “endianness”) mô tả cách máy tính sắp xếp thứ tự byte khi lưu trữ hay xử lý một số nhiều byte (multi-byte number).

Ví dụ dễ hiểu nhất là số `0x12345678`.
Hai kiểu chính:

| Kiểu          | Thứ tự byte trong bộ nhớ | Ý nghĩa                               |
| ------------- | ------------------------ | ------------------------------------- |
| Big-endian    | `12 34 56 78`            | Byte lớn (big end) được lưu trước.    |
| Little-endian | `78 56 34 12`            | Byte nhỏ (little end) được lưu trước. |
Trong code:

`m_int = int.from_bytes(text.encode('utf-8'), byteorder='big')`

Ta chọn `"big"` nghĩa là byte đầu tiên của chuỗi là phần có trọng số cao nhất trong số nguyên.
Ví dụ:

```
text = "AB"
text.encode('utf-8')  # b'AB' = [65, 66]
```

Nếu `byteorder='big'`: `m_int = 65 * 256 + 66 = 16706`
Nếu `byteorder='little'`: `m_int = 66 * 256 + 65 = 16961`
-> cùng một chuỗi `"AB"` nhưng hai hướng đọc khác nhau cho ra hai số khác nhau.
Vì RSA hoạt động trên biểu diễn toán học và ta muốn thứ tự byte tự nhiên từ trái sang phải.