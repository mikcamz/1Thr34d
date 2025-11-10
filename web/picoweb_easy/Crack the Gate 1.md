#### Description

We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: `ctf-player@picoctf.org`. Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?The website is running [here](http://amiable-citadel.picoctf.net:55010/). Can you try to log in?

Hints:
1) Developers sometimes leave notes in the code; but not always in plain text.
2) A common trick is to rotate each letter by 13 positions in the alphabet.

---


Ta thấy đoạn mã bí ẩn:

![[Pasted image 20251110112001.png]]

Giải mã ROT13 ta được:
`NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"`

Mình mở Burp lên, quẳng link vô Chromium bên tab Proxy, sau đó ấn Forward, rồi nhập email với password bên Chromium.

Sau đó thêm `X-Dev-Access: yes` vào đây:

![[Pasted image 20251110112150.png]]

Ấn Forward thì sẽ hiện thông báo:

![[Pasted image 20251110112842.png]]

Bạn cũng có thể qua tab Target để xem Response nhá:

![[Pasted image 20251110112945.png]]

=> `picoCTF{brut4_f0rc4_49d1d186}`