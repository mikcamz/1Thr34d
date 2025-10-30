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

e = 65537  # || e = 17 || e = 3
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

# kiểm tra m-int < N (điều kiện RSA)
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

'''
Ta có:
ciphertext = c
plaintext = m = 42 # dạng số

Mã hóa;
=> c = m^e % N

Giải mã:
=> m = c^d % N
'''
