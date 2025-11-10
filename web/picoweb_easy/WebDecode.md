#### Description

Do you know how to use the web inspector?Start searching [here](http://titan.picoctf.net:59256/) to find the flag

Hints:
1) Use the web inspector on other files included by the web page.
2) The flag may or may not be encoded

---

OK mình mở F12 lên để inspect web này.

<img width="1449" height="1218" alt="Pasted image 20251110101346" src="https://github.com/user-attachments/assets/9051177c-52b6-4e81-99e3-28a59a982e04" />


Hiện tại ta đang ở trang chủ `HOME` và mình đã kiểm tra code html và css thì không thấy gì đặc biệt cả nên mình đã nhảy sang trang `ABOUT` để kiểm tra tiếp, thì mình phát hiện ra đoạn mã có mùi =)) (hình như là được encode base64).

<img width="1443" height="1153" alt="Pasted image 20251110101602" src="https://github.com/user-attachments/assets/3ab30537-953a-44f0-a4c3-ada9fc9af41f" />


Giải mã thì mình được flag:

=> `picoCTF{web_succ3ssfully_d3c0ded_10f9376f}`
