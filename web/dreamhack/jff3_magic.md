# [wargame.kr] jff3_magic
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/7a7809f4c691a25735a7d3c3a5151a6bbf3619c96f52f342a214ce0de87a5028.png)

Hint: swp: (vim swap file)
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/3d4fb23ab15df8d9b7fa4fd34ae7c70859e0f99a55e96b943dbce9f6fc8191c9.png)

using strings to extract the code:
```bash
strings .index.php.swp > code.php
```

![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/c34536e65e322283656fbc350885093894c459376736fec480e1eb7a549d268f.png)
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/f33f2848329c05c952987c1692ceab1fdbfbc871bd5b48fff71acedf3c2110ff.png)

Web loose compare password => PHP loose comparision attack. There are magic hashes that when hashed, turns into `0e987143091345...`, which php will interpret as float (or `False` when compare with another string).

In some case (this case), the password hash checking is done improperly, resulting in the web comparing 0 with 0 = TRUE

From the leaked index.php code, we can see that the web use `haval128,5` for it's password encryption and loosely compare that float value with the user pw hash.

I lookup for `haval128,5` magic hash value and find this doc: https://aceatom.tistory.com/15
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/71bab705eff47be33fd0240a08a22d523b1ea147cccd9191a1f79803b2c0728d.png)

When submit as password with admin username:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/9a515dfef4f634e3eff8a09055f242ff3a2990d269875430e864b7f5d281bacc.png)
