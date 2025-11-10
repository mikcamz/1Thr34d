#### Description

Try [here](http://titan.picoctf.net:51633/) to find the flag

Hints:
1) Try using burpsuite to intercept request to capture the flag.
2) Try mangling the request, maybe their server-side code doesn't handle malformed requests very well.

#burpsuite

---

Bài này mô phỏng cho ta cách hoạt động khi mà mình đăng nhập và vượt 2FA.

Vô bài thì mình nhập bla bla:

![[Pasted image 20251109111617.png]]

Sau đó nó sẽ hiện trang nhập mã OTP (one time password), mình nhập đại `1234`:

![[Pasted image 20251109111808.png]]

Uầy đương nhiên là sai ròi:

![[Pasted image 20251109111824.png]]

Và mình sẽ dùng Burp để tìm hiểu nhá:

![[Pasted image 20251109112002.png]]

Chuyển code qua công cụ Repeater.
Và mình thấy đây là đoạn code được chuyển đi với phương thức POST.

Và POST dùng để gửi dữ liệu đến máy chủ nhằm tạo mới hoặc cập nhật một tài nguyên.
So sánh giữa GET và POST: 

| Đặc điểm       | Phương thức GET                                 | Phương thức POST                             |
| ------------------ | --------------------------------------------------- | ------------------------------------------------ |
| Mục đích       | Yêu cầu, _lấy_ dữ liệu từ server.                   | Gửi, _đẩy_ dữ liệu lên server.                   |
| Vị trí dữ liệu | Trên URL (query string).                        | Trong Body của request.                      |
| Hiển thị       | Hiển thị công khai trên URL, bookmark, lịch sử. | Ẩn, không thấy trên URL.                     |
| Ví dụ          | `GET /search?user=admin`                            | `POST /login`                                    |
| An toàn (CTF)  | Dễ thấy, nhưng cũng dễ bị WAF/filter chặn.          | "Giấu" payload. Đây là nơi bạn chèn SQLi, XSS... |

Vì vậy mình đơn giản chỉ cần thay đổi mã OTP theo đúng là được.. Thay vì nhập số, thì mình nhập chuỗi và vẫn bị trả về `invalid otp`, từ đó mình thấy dường như máy chủ không phân biệt số hay chuỗi chữ.

Loay hoay một hồi mình xóa nó luôn và gửi lại request đến server là lụm flag ngay phần response:

![[Pasted image 20251109112449.png]]

=> `picoCTF{#0TP_Bypvss_SuCc3$S_2e80f1fd}`