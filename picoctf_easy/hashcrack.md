>A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
>Additional details will be available after launching your challenge instance.

## The lazy and realistic way
Connecting to the server using the provided command, we are provided with the hash:
<img width="674" height="135" alt="Pasted image 20251020090557" src="https://github.com/user-attachments/assets/9e8ff3da-0600-496b-b55d-7d4b270592a5" />


In this approach i use an online hash crack service, this site db contains alot of already cracked password, we are basically querying this hash. Luckly the hash has been cracked:
<img width="1870" height="1041" alt="Pasted image 20251020092135" src="https://github.com/user-attachments/assets/2918506d-4976-434b-b43d-00b67299c7d1" />

Do this for all the hash we get, we eventually get the flag:
<img width="1084" height="394" alt="Pasted image 20251020092020" src="https://github.com/user-attachments/assets/351d23b5-ee3f-4751-a846-e0a9ad8a72ac" />

## The proper way (intended)
>MD5: The length of MD5 hash is 32 characters
>SHA1: The length of SHA1 hash is 40 characters
>SHA256: The length of SHA256 hash is 64 characters

Instead of using an online service, we will bruteforce the hash ourselve in this approach using `johntheripper`
First hash is MD5, we know that from the length, so the command will be:
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=raw-md5 hash.txt
```
<img width="1010" height="234" alt="Pasted image 20251020094100" src="https://github.com/user-attachments/assets/d2ebaa6b-fa7b-4a84-8196-136ed96a4623" />
We do that for all other hashes, changing the format accordingly and get the flag
