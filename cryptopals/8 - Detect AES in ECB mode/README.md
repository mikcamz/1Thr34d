Ta được cho một file txt chứa một nùi ciphertext được mã hóa hex. Trong số dòng đó có 1 dòng bị encrypted với AES-ECB. Tìm ra dòng đó?

Hướng suy nghĩ:
AES-ECB làm việc với từng block 16 byte độc lập. Nếu trong một ciphertext (một dòng) có block nào lặp nhiều lần -> ciphertext sẽ có chính xác các block ciphertext lặp.

Ban đầu tôi định nối tất cả thành một chuỗi dài rồi đếm block trùng, nhưng mà nhận ra mình sẽ:
- Pha trộn nhiều ciphertext khác nhau, gây ra false positives (các block từ ciphertext A trùng block ở ciphertext B không có nghĩa A dùng ECB).
- Sai ý đề bài:>>

Do đó với mỗi ciphertext hex mình sẽ:
- decode hex -> bytes
- chia thành block 16-byte
- đếm block trùng (dùng `Counter)
- score = tổng block - số block khác nhau (số block lặp)
- chọn dòng có score lớn nhất (hoặc >0)

Code đây:

```
from collections import Counter, defaultdict
  
BLOCK = 16  # AES block size

def ecb_score_from_hex(line_hex):
    # Chia ciphertext hex thành các block 16 byte và tính số block bị lặp
    data = bytes.fromhex(line_hex.strip())
    blocks = [data[i:i+BLOCK] for i in range(0, len(data), BLOCK)]

    # lấy số blocks tổng trừ số blocks duy nhất ra số block thừa
    return len(blocks) - len(set(blocks)), blocks

# Đọc file và loại bỏ dòng rỗng
with open("8.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

# Biến lưu dòng có số block trùng nhiều nhất
best = {"idx": None, "score": -1, "blocks": None, "hex": None}

# Duyệt từng dòng, hàm enumerate() để lấy chỉ số dòng, không cần biến đếm ngoài
for i, line in enumerate(lines):
    score, blocks = ecb_score_from_hex(line)
    if score > best["score"]:
        best = {"idx": i, "score": score, "blocks": blocks, "hex": line}

print("Dòng chứa mã hóa AES-ECB:", best["idx"])
print("Số block thừa:", best["score"])
print("Ciphertext (hex):", best["hex"])

# Dùng defaultdict để lưu vị trí xuất hiện của từng block
positions = defaultdict(list)

# Ghi lại vị trí từng block
for j, b in enumerate(best["blocks"]):
    # lưu bị trí j của block b (hex)
    positions[b.hex()].append(j)

# In ra block nào xuất hiện nhiều hơn 1 lần
print("\nCác block bị trùng trong dòng nghi ngờ:")
for block_hex, idxs in positions.items():
    if len(idxs) > 1:
        print(f"Block {block_hex} xuất hiện {len(idxs)} lần tại vị trí {idxs}")
```

=>
```
Dòng chứa mã hóa AES-ECB: 132
Số block thừa: 3
Ciphertext (hex): d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a

Các block bị trùng trong dòng nghi ngờ:
Block 08649af70dc06f4fd5d2d69c744cd283 xuất hiện 4 lần tại vị trí [1, 3, 5, 7]
```
