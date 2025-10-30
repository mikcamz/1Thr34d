from collections import Counter, defaultdict

BLOCK = 16  # AES block size

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
