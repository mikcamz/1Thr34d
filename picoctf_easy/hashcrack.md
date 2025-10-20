>A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
>Additional details will be available after launching your challenge instance.

## The lazy and realistic way
Connecting to the server using the provided command, we are provided with the hash:
![[Pasted image 20251020090557.png]]

In this approach i use an online hash crack service, this site db contains alot of already cracked password, we are basically querying this hash. Luckly the hash has been cracked:
![[Pasted image 20251020092135.png]]

Do this for all the hash we get, we eventually get the flag:
![[Pasted image 20251020092020.png]]

## The proper way (intended)
>MD5: The length of MD5 hash is 32 characters
>SHA1: The length of SHA1 hash is 40 characters
>SHA256: The length of SHA256 hash is 64 characters

Instead of using an online service, we will bruteforce the hash ourselve in this approach using `johntheripper`
First hash is MD5, we know that from the length, so the command will be:
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 hash.txt
```
![[Pasted image 20251020094100.png]]
We do that for all other hashes, changing the format accordingly and get the flag