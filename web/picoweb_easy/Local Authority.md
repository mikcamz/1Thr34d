#### Description

Can you get the flag?Go to this [website](http://saturn.picoctf.net:55072/) and see what you can discover.

Hint:
How is the password checked on this website?

---

Đọc tên tiêu đề và hint mình cũng thấy tác giả đang muốn đề cập đến một cái local password validation function trong bài này rồi.

Như thường lệ mình mở link lên để ngắm ngía..

![[Pasted image 20251110082502.png]]

Mình nhập đại tên và mật khẩu (tất nhiên là trả vè kết quả sai ròi:> ):

![[Pasted image 20251110082715.png]]

Sau đó ấn F12 để inspect nội dung web, và thấy một hàm js để check giá trị username và password người dùng nhập vào, để so sánh và đối chiếu với giá trị username/password cố định (có sẵn). 

![[Pasted image 20251110083141.png]]

Và lúc này mình nghi có thể 2 giá trị cố định này được đặt đâu đó, có thể note ở css hoặc là file js đính kèm, nên mình mới nhảy sang tab `Sources` để kiểm tra toàn bộ files và mình thấy thứ cần tìm:

![[Pasted image 20251110083338.png]]

Giờ chỉ cần quay lại web ban đầu, nhập `admin` và `strongPassword098765` là lụm flag..

![[Pasted image 20251110083456.png]]

=> `picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}`