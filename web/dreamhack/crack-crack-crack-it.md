# crack crack crack it
This challenge involves bruteforcing a MD5-crypt hash

hash can found inside the .htaccess file downloadable after starting instance

## Solve
### Hash identifier
Used an online hash identifier:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/26f740c661e6b6606446fd7d34b7779e5aca4d021d284f11a9aa6c06c2149d1b.png)
Hash type matches with hashcat mode 500

### Hashcat bruteforce
```bash
hashcat -m 500 -a 3 -1 "?d?l" '$1$zQeDWhxJ$qYfMRImvL9tRj.hUCZ3d31' "G4HeulB?1?1?1?1"
```

`-1 "?d?l"`: custom charset contain number and lowercase letters
`"G4HeulB?1?1?1?1"`: the prefix provided on the web follows by 4 char in the charset (try 1 char, then 2, then 3, then 4)



