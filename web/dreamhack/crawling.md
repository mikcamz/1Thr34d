# crawling
This challenge involves a DNS rebinding attack

Code:
```python
def lookup(url):
    try:
        return socket.gethostbyname(url)
    except:
        return False

def check_global(ip):
    try:
        return (ipaddress.ip_address(ip)).is_global
    except:
        return False

def check_get(url):
    ip = lookup(urlparse(url).netloc.split(':')[0])
    if ip == False or ip =='0.0.0.0':
        return "Not a valid URL."
    res=requests.get(url)
    if check_global(ip) == False:
        return "Can you access my admin page~?"
    for i in res.text.split('>'):
        if 'referer' in i:
            ref_host = urlparse(res.headers.get('refer')).netloc.split(':')[0]
            if ref_host == 'localhost':
                return False
            if ref_host == '127.0.0.1':
                return False 
    res=requests.get(url)
    return res.text

@app.route('/admin')
def admin_page():
    if request.remote_addr != '127.0.0.1':
    		return "This is local page!"
    return app.flag

@app.route('/validation')
def validation():
    url = request.args.get('url', '')
    ip = lookup(urlparse(url).netloc.split(':')[0])
    res = check_get(url)
    return render_template('validation.html', url=url, ip=ip, res=res)
```

In `check_get()`:
- I have to provide a global ip for the check to pass 
- The referer filter below is faulty since it checks the header 'refer' not 'referer'.

## Solve
The script does a 'preflight' check of the ip address to see if it is global or not:
```python
def check_get(url):
    ip = lookup(urlparse(url).netloc.split(':')[0])
    if ip == False or ip =='0.0.0.0':
        return "Not a valid URL."
    if check_global(ip) == False:
        return "Can you access my admin page~?"
```
And then if the ip resolve to a global one, it fetch the url after:
```python
res=requests.get(url)
return res.text
```

This is vulnerable to **DNS rebinding attack** where an attacker change the dns of his site randomly, with the goal of tricking the preflight ip check to resolve to a global ip, then change dns to the local ip.

We use the website of this github repo to test this quicker, without setting up our own server: `https://github.com/taviso/rbndr` -> `rbndr.us`
This site will switch randomly between the 2 ip address we provided
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/c77fee4a87335866e24b06e6309889597d7c909bc71cd1defa73b6e315a781f3.png)

Then send this url to the /validate endpoint and retry multiple time to get the flag
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/1c2011309f346809fe9f12ce06214d29f3a515cf9213a3d59812cbdbb4e2c56a.png)
