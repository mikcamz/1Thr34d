#### Description

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:45028/](http://mercury.picoctf.net:45028/)

Hints:
1) Maybe you have more than 2 choices
2) Check out tools like Burpsuite to modify your requests and look at the responses

---

Nhìn vô thì thấy đây là một trang web không có gì đặc biệt, khi chọn `Red` hay `Blue` thì cũng không có gì thay đổi trong code (mình đã mở `F12/elements` lên xem)

Khi đọc đề và kết hợp hints tác giả cho thì mình nhận thấy trong bài này, tác giả đang muốn đề cập đến GET/HEAD. Đây là hai phương thức yêu cầu HTTP khác nhau:
- GET dùng để yêu cầu lấy toàn bộ dữ liệu của một tài nguyên từ máy chủ.
- HEAD chỉ yêu cầu lấy siêu dữ liệu (tiêu đề) về tài nguyên đó mà không cần tải xuống nội dung chính. Để kiểm tra tính khả dụng hoặc kích thước của một tệp trước khi tải về.

Từ đó mình mới vào Burp Suite để kiểm tra:
Đầu tiên mình vào `Target` để nhập link lên browser của Burp.

![[Pasted image 20251108162424.png]]

Sau đó mình qua `Proxy` và chuyển phần `Request` qua công cụ `Repeater`:

![[Pasted image 20251108162612.png]]

Các bạn thấy đầu GET thì sẽ tải về tài nguyên của máy chủ:

![[Pasted image 20251108162822.png]]

Nên là khi đổi qua đầu HEAD thì nó sẽ trả về title của máy chủ, và ta tìm thấy flag:

![[Pasted image 20251108162714.png]]

=> `picoCTF{r3j3ct_th3_du4l1ty_775f2530}`