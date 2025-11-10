#### Description

There is some interesting information hidden around this site [http://mercury.picoctf.net:5080/](http://mercury.picoctf.net:5080/). Can you find it?

Hint:
You should have enough hints to find the files, don't run a brute forcer.

#recon #reconnaissance #apache 

---

Vô đọc hint là thấy mình phải làm từng bước từng bước => flag được chia ra thành nhiều phần và mình phải đi gom lại.

Đầu tiên nhấp vô link, thì hiện ra site khá bình thường, vào kiểm tra thì thấy mảnh đầu tiên của flag:

<img width="1373" height="447" alt="Pasted image 20251109100310" src="https://github.com/user-attachments/assets/717a06bd-c1e4-45a4-823d-896c93e14759" />


-> `picoCTF{t`

Có mảnh thứ 2 trong `mycss.css`:

<img width="768" height="814" alt="Pasted image 20251109100428" src="https://github.com/user-attachments/assets/52311c5a-6c0b-4260-a573-f1dfc395bcc3" />


-> `h4ts_4_l0`

Kiểm tra `myjs.js` thì thấy hint thứ 2:
**How can I keep Google from indexing my website?**

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

Vậy thì giờ mình chỉ cần thêm `/robots.txt` vào đuôi của url thôi:

<img width="807" height="211" alt="Pasted image 20251109101305" src="https://github.com/user-attachments/assets/f50ef185-b7ac-4d4f-91f4-51db22ef46cc" />


-> Cấm tất cả bot vào `index.html`.
-> mảnh thứ 3: `t_0f_pl4c`

Và có hint thứ 3:
**I think this is an apache server... can you Access the next flag?**

Với keywords "apache" và "Access" thì mình tìm hiểu được như sau:

1) Apache
- Là web server software phổ biến trên thế giới (cạnh tranh với Nginx).
- Nhiệm vụ: khi mình truy cập `http://example.com` vào trình duyệt, thì trình duyệt sẽ gửi request đến máy chủ. Apache sẽ nhận yêu cầu và tìm tệp (ví dụ: `index.html`) và gửi tệp đó trở lại tình duyệt của mình để hiển thị.

2) Access Control (AC) (kiểm soát truy cập)
- AC là quát trình xác định ai được phép làm gì.
- Gồm: đối tượng chỉ thị, nhiệm vụ và luật (rules).

Khi kết hợp cả hai lại, thì đây là cách mà máy chủ web Apache thực thi rules để kiểm soát ai được xem nội dung nào. Mình tìm hiểu được 2 khái niệm:
1) Cấu hình trung tâm (file `httpd.conf`): đặt rules chung cho toàn bộ (nhiều) websites.
2) Cấu hình phân tán (file `.htaccess`): đặt trong chính các thư mục của website; cho phép devs override hoặc bổ sung các quy tắc riêng cho thư mục mẹ và thư mục con mà không cần đụng đến file cấu hình chính `httpd.conf`.

Vậy với hint 3, mình sẽ xóa `/robots.txt` và thêm `.htaccess` vào đuôi của url:

<img width="816" height="202" alt="Pasted image 20251109102958" src="https://github.com/user-attachments/assets/91942614-c307-4bf3-8d9c-cf566b270a33" />


-> mảnh thứ 4: `3s_2_lO0k`

Và có hint thứ 4:
**I love making websites on my Mac, I can Store a lot of information there.**

Với keyword "Mac" và "Store" thì mình biết được hint 4 đang chỉ thẳng đến file `.DS_Store`.

- `.DS_Store` là viết tắt của "Desktop Services Store".
- Là một file ẩn (bắt đầu bằng dấu `.`) được hđh macOS tự động tạo ra trong mọi thư mục mà người dùng truy cập bằng Finder (trình duyệt file của Mac).
- Công dụng: để store các metadata của thư mục đó (ví dụ: vị trí icons, bg-image, dạng tên file,...)

Vậy thì giờ chỉ cần xóa `.htaccess` và thêm `.DS_Store` vào và ấn Enter:

<img width="790" height="183" alt="Pasted image 20251109103947" src="https://github.com/user-attachments/assets/766dc463-4076-44fa-8982-b34cb6ad12ac" />


-> Mảnh cuối cùng: `_35844447}`

=> Flag: `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}`
