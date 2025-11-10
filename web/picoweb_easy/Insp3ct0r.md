#### Description

Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/9670/` ([link](https://jupiter.challenges.picoctf.org/problem/9670/)) or http://jupiter.challenges.picoctf.org:9670

Hints:
1) How do you inspect web code on a browser?
2) There's 3 parts

---

Link mở ra một trang hiển thị như vầy:

![[Pasted image 20251108102934.png]]

![[Pasted image 20251108102950.png]]

Tui sẽ mở F12 lên examine nó tí.
Mở phần `Sources` để những file như html, js, css (thứ tạo nên site như tác giả nói).

Đầu tiên với file html thì tôi đã tìm thấy phần 1 của flag: `picoCTF{tru3_d3`

![[Pasted image 20251108103430.png]]

Nhảy qua css thì thấy phần 2: `t3ct1ve_0r_ju5t`

![[Pasted image 20251108103513.png]]

Và ở js, thấy phần cuối: `_lucky?2e7b23e3}`

![[Pasted image 20251108103603.png]]

-> với hint 2 gợi ý flag có 3 phần: 
=> `picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}