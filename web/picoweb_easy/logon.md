#### Description

The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/13594/` ([link](https://jupiter.challenges.picoctf.org/problem/13594/)) or http://jupiter.challenges.picoctf.org:13594

Hint;
Hmm it doesn't seem to check anyone's password, except for Joe's?

---

Khi nhấp vào link, mình được web thế này:

![[Pasted image 20251108110117.png]]

Và vấn đề hiện ra là, đề bài kêu mình đăng nhập dưới quyền Joe có thể log in vào web, nhưng mà khi mình nhập tên là Joe với một password ngẫu nhiên thì nó không vào được:

![[Pasted image 20251108110259.png]]

Với hint: `Hmm it doesn't seem to check anyone's password, except for Joe's?`, vậy thì giờ mình nhập tên khác và pass ngẫu nhiên thôi, site nó chỉ chặn không cho đăng nhập dưới tên `Joe`.

![[Pasted image 20251108110525.png]]

Mở F12 lên inspect cách FE tương tác với BE. Mình nhảy sang kênh Network thì thấy nhiều điều lý thú:

![[Pasted image 20251108110845.png]]

![[Pasted image 20251108110900.png]]

Nên giờ mình thử copy dưới dạng cURL (cmd), đem ra text editor sửa `admin=False` thành `admin=True` rồi curl đến server.

![[Pasted image 20251108111137.png]]

Và mình tìm thấy flag:
=> `picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}`