#### Description

The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/13594/` ([link](https://jupiter.challenges.picoctf.org/problem/13594/)) or http://jupiter.challenges.picoctf.org:13594

Hint;
Hmm it doesn't seem to check anyone's password, except for Joe's?

---

Khi nhấp vào link, mình được web thế này:

<img width="1277" height="693" alt="Pasted image 20251108110117" src="https://github.com/user-attachments/assets/18b3db71-3553-4841-8859-65e4096dbd1f" />

Và vấn đề hiện ra là, đề bài kêu mình đăng nhập dưới quyền Joe có thể log in vào web, nhưng mà khi mình nhập tên là Joe với một password ngẫu nhiên thì nó không vào được:

<img width="1277" height="688" alt="Pasted image 20251108110259" src="https://github.com/user-attachments/assets/52e7d5d8-58e4-4b62-ae4f-323fc1479909" />

Với hint: `Hmm it doesn't seem to check anyone's password, except for Joe's?`, vậy thì giờ mình nhập tên khác và pass ngẫu nhiên thôi, site nó chỉ chặn không cho đăng nhập dưới tên `Joe`.

<img width="1276" height="550" alt="Pasted image 20251108110525" src="https://github.com/user-attachments/assets/fde5e06b-4470-444e-b02c-eb63786305f5" />

Mở F12 lên inspect cách FE tương tác với BE. Mình nhảy sang kênh Network thì thấy nhiều điều lý thú:

<img width="1319" height="1081" alt="Pasted image 20251108110845" src="https://github.com/user-attachments/assets/d17b4880-7a9c-4f38-b39b-7b8db21add89" />

<img width="926" height="69" alt="Pasted image 20251108110900" src="https://github.com/user-attachments/assets/ec6e15d6-540c-4a58-8984-a083d6a4b631" />

Nên giờ mình thử copy dưới dạng cURL (cmd), đem ra text editor sửa `admin=False` thành `admin=True` rồi curl đến server.

<img width="1939" height="825" alt="Pasted image 20251108111137" src="https://github.com/user-attachments/assets/bcfa0477-e55f-43e1-bbc8-a9612b7caaac" />

Và mình tìm thấy flag:
=> `picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}`
