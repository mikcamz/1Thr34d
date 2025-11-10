#### Description

Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/9670/` ([link](https://jupiter.challenges.picoctf.org/problem/9670/)) or http://jupiter.challenges.picoctf.org:9670

Hints:
1) How do you inspect web code on a browser?
2) There's 3 parts

---

Link mở ra một trang hiển thị như vầy:

<img width="1277" height="569" alt="Pasted image 20251108102934" src="https://github.com/user-attachments/assets/40657c6f-739a-43bb-be66-50fb2388a597" />


<img width="1277" height="582" alt="Pasted image 20251108102950" src="https://github.com/user-attachments/assets/7d591864-3c2e-4458-8030-4e1c0f6f71a8" />


Tui sẽ mở F12 lên examine nó tí.
Mở phần `Sources` để những file như html, js, css (thứ tạo nên site như tác giả nói).

Đầu tiên với file html thì tôi đã tìm thấy phần 1 của flag: `picoCTF{tru3_d3`

<img width="641" height="700" alt="Pasted image 20251108103430" src="https://github.com/user-attachments/assets/48a9130d-cfec-485a-8ce7-a0ab352f8fce" />


Nhảy qua css thì thấy phần 2: `t3ct1ve_0r_ju5t`

<img width="612" height="850" alt="Pasted image 20251108103513" src="https://github.com/user-attachments/assets/c48a00bf-92d1-4b53-a50f-053b7610a29a" />


Và ở js, thấy phần cuối: `_lucky?2e7b23e3}`

<img width="615" height="452" alt="Pasted image 20251108103603" src="https://github.com/user-attachments/assets/26ab8af7-3342-4e73-a0c1-ebea2ad49221" />


-> với hint 2 gợi ý flag có 3 phần: 
=> `picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}
