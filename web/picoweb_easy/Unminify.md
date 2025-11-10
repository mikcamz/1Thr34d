I don't like scrolling down to read the code of my website, so I've squished it. As a bonus, my pages load faster!
Browse [here](http://titan.picoctf.net:65033/), and find the flag!

Hints:
1) Try CTRL+U / ⌘+U in your browser to view the page source. You can also add 'view-source:' before the URL, or try `curl <URL>` in your shell.
2) Minification reduces the size of code, but does not change its functionality.
3) What tools do developers use when working on a website? Many text editors and browsers include formatting.

---

Cách 1:

Ctrl + U để đọc code, thì thấy code này được dàn trải ra trên một dòng, sau đó tôi dùng Ctrl + F, gõ key "picoCTF{" để tìm flag, và tôi thấy nó:

![[Pasted image 20251110092502.png]]

=> `picoCTF{pr3tty_c0d3_743d0f9b}`


Cách 2:

Mình sẽ làm theo cách hint chỉ là `curl <URL>`, vậy giờ mình chỉ cần mở cmd lên quẳng lệnh này vô:

Với WSL2 (Bash):

```
curl http://titan.picoctf.net:65033/ | grep "picoCTF{"
```

Với CMD:

```
curl http://titan.picoctf.net:65033/ | findstr "picoCTF{"
```

*Note*: bỏ phần `http://` cũng được vì `curl` mặc định sử dụng giao thức HTTP, nhưng với các kết nối như HTTPS hay FTP, SCP, POP3,.. thì ghi vào.

=> `picoCTF{pr3tty_c0d3_743d0f9b}`