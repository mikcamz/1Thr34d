#### Description

Do you know how to use the web inspector?Start searching [here](http://titan.picoctf.net:59256/) to find the flag

Hints:
1) Use the web inspector on other files included by the web page.
2) The flag may or may not be encoded

---

OK mình mở F12 lên để inspect web này.

![[Pasted image 20251110101346.png]]

Hiện tại ta đang ở trang chủ `HOME` và mình đã kiểm tra code html và css thì không thấy gì đặc biệt cả nên mình đã nhảy sang trang `ABOUT` để kiểm tra tiếp, thì mình phát hiện ra đoạn mã có mùi =)) (hình như là được encode base64).

![[Pasted image 20251110101602.png]]

Giải mã thì mình được flag:

=> `picoCTF{web_succ3ssfully_d3c0ded_10f9376f}`