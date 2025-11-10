#### Description

Can you find the robots? `https://jupiter.challenges.picoctf.org/problem/60915/` ([link](https://jupiter.challenges.picoctf.org/problem/60915/)) or http://jupiter.challenges.picoctf.org:60915

Hint:
What part of the website could tell you where the creator doesn't want you to look?

#robots

---

Khi nhấp vào link thì mở ra một trang trống với tiêu đề:

<img width="1276" height="507" alt="Pasted image 20251108102336" src="https://github.com/user-attachments/assets/f34b375f-aeff-4324-a359-76820751f163" />

Bây giờ từ “robot” khiến mình liên tưởng đến các tệp `robots.txt` khi nói đến việc giải CTF. Cộng với hint: `What part of the website could tell you where the creator doesn't want you to look?`.

Sau khi tìm hiểu thì mình thấy hint này chỉ mình đến file `robots.txt`.

`robots.txt` là một file văn bản đơn giản được đặt ở thư mục gốc (root) của một website (ví dụ: `https://example.com/robots.txt`).

Công dụng thật: File này được dùng để "ra lệnh" cho các con bot (web crawlers) hợp pháp, đặc biệt là của các công cụ tìm kiếm như Google (Googlebot), Bing,...
- Nó cho bot biết thư mục hoặc file nào chúng **không nên** truy cập hoặc index (lập chỉ mục).
	Ví dụ, admin không muốn Google index trang quản trị, thư mục chứa ảnh tạm, hoặc các trang kết quả tìm kiếm nội bộ.
    
Cú pháp của nó rất đơn giản:

```
User-agent: [tên-con-bot]
Disallow: [đường-dẫn-không-được-vào]
```

- `User-agent: *` (dấu sao) nghĩa là "áp dụng cho tất cả các bot".
- `Disallow: /admin/` nghĩa là "cấm bot vào vào thư mục `/admin/`".

Vì vậy, mình truy cập tệp `robots.txt` bằng cách thêm `/robots.txt` vào URL của trang web. Đây là những gì mình nhận được:

<img width="981" height="262" alt="Pasted image 20251108102754" src="https://github.com/user-attachments/assets/8a3685bf-f00b-400b-a0c5-9d2a866947f3" />

=> `picoCTF{ca1cu1at1ng_Mach1n3s_8028f}`
