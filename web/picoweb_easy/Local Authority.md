#### Description

Can you get the flag?Go to this [website](http://saturn.picoctf.net:55072/) and see what you can discover.

Hint:
How is the password checked on this website?

---

Đọc tên tiêu đề và hint mình cũng thấy tác giả đang muốn đề cập đến một cái local password validation function trong bài này rồi.

Như thường lệ mình mở link lên để ngắm ngía..

<img width="621" height="305" alt="Pasted image 20251110082502" src="https://github.com/user-attachments/assets/1830e7cc-5606-44c5-a669-3a634ac32fd0" />


Mình nhập đại tên và mật khẩu (tất nhiên là trả vè kết quả sai ròi:> ):

<img width="573" height="196" alt="Pasted image 20251110082715" src="https://github.com/user-attachments/assets/3ffcaa44-fff1-402a-a38e-3a58d0faa679" />


Sau đó ấn F12 để inspect nội dung web, và thấy một hàm js để check giá trị username và password người dùng nhập vào, để so sánh và đối chiếu với giá trị username/password cố định (có sẵn). 

<img width="1288" height="1097" alt="Pasted image 20251110083141" src="https://github.com/user-attachments/assets/ae05e451-64ce-4178-a24a-89ab017fb2ca" />


Và lúc này mình nghi có thể 2 giá trị cố định này được đặt đâu đó, có thể note ở css hoặc là file js đính kèm, nên mình mới nhảy sang tab `Sources` để kiểm tra toàn bộ files và mình thấy thứ cần tìm:

<img width="842" height="332" alt="Pasted image 20251110083338" src="https://github.com/user-attachments/assets/af599265-73ac-4d8e-9296-af921ae1fde6" />


Giờ chỉ cần quay lại web ban đầu, nhập `admin` và `strongPassword098765` là lụm flag..

<img width="610" height="183" alt="Pasted image 20251110083456" src="https://github.com/user-attachments/assets/e71fcce9-f647-4d70-961e-f1a6065d4c6b" />


=> `picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}`
