#### Description

Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?You can access the Cookie Monster [here](http://verbal-sleep.picoctf.net:63856/) and good luck

Hints:
1) Sometimes, the most important information is hidden in plain sight. Have you checked all parts of the webpage?
2) Cookies aren't just for eating - they're also used in web technologies!
3) Web browsers often have tools that can help you inspect various aspects of a webpage, including things you can't see directly.

#cookie

---

Nhập bla bla bla gì đó thì nó sẽ dẫn bạn đến đây:

<img width="574" height="188" alt="Pasted image 20251110102023" src="https://github.com/user-attachments/assets/2b90739e-f76c-44b2-b8c2-36db9fed2a0c" />


Ok thì giờ mình đi tìm cookie thôi.
Tui chạy thẳng vào tab `Network` thì thấy biến `secret_recipe` đập vào mắt:

<img width="1085" height="1107" alt="Pasted image 20251110102231" src="https://github.com/user-attachments/assets/c8a3d7b3-e02e-44dc-a664-760f45f8ca22" />


Hoặc bạn có thể vào bên `Application` để tìm nó cũng được:

<img width="1349" height="1107" alt="Pasted image 20251110102410" src="https://github.com/user-attachments/assets/812dac45-cecb-4b71-a028-8597569eb10e" />


Hình như là được encode bằng base64 `cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzQ3MzZGNkNCfQ`

Giải xong được flag:

=> `picoCTF{c00k1e_m0nster_l0ves_c00kies_4736F6CB}`
