# MD5 password
This challenge involves a preimage MD5 raw-bytes sql injection
Credit goes to this blog: https://cvk.posthaven.com/sql-injection-with-raw-md5-hashes

# Solve
The code:
```php
select * from admin_password where password='".md5($ps,true)."'
```
The `true` argument make the md5 function return raw bytes, which is dangerous for SQL since it contains bytes that are `" / ' | # ...`

Our goal is to find a string that when hash with MD5 turns into rawbyte sqli payload 

The blogs contain multiple optimization steps to shorten the sqli payload (to reduce complexity of calculating preimage of md5 hash) and bruteforcing the hash that will turn into a sqli payload:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/8a2bfa5b2dd78f644cb02f4af402f8bf1c188da84feacd8ac2f5d0407182d6c9.png)

The hash is `129581926211651571912466741651878684928`, this will grants us the flag
That will resolve into raw MD5 hash: `?T0D??o#??'or'8.N=?`

Note the `'or'8`, this is the same as `'||'1` or `' or 1` in SQL 
