#### Description

There is some interesting information hidden around this site [http://mercury.picoctf.net:5080/](http://mercury.picoctf.net:5080/). Can you find it?

Hint:
You should have enough hints to find the files, don't run a brute forcer.

#recon #reconnaissance #apache 

---

Vô đọc hint là thấy mình phải làm từng bước từng bước => flag được chia ra thành nhiều phần và mình phải đi gom lại.

Đầu tiên nhấp vô link, thì hiện ra site khá bình thường, vào kiểm tra thì thấy mảnh đầu tiên của flag:

![[Pasted image 20251109100310.png]]

-> `picoCTF{t`

Có mảnh thứ 2 trong `mycss.css`:

![[Pasted image 20251109100428.png]]

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

![[Pasted image 20251109101305.png]]

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

![[Pasted image 20251109102958.png]]

-> mảnh thứ 4: `3s_2_lO0k`

Và có hint thứ 4:
**I love making websites on my Mac, I can Store a lot of information there.**

Với keyword "Mac" và "Store" thì mình biết được hint 4 đang chỉ thẳng đến file `.DS_Store`.

- `.DS_Store` là viết tắt của "Desktop Services Store".
- Là một file ẩn (bắt đầu bằng dấu `.`) được hđh macOS tự động tạo ra trong mọi thư mục mà người dùng truy cập bằng Finder (trình duyệt file của Mac).
- Công dụng: để store các metadata của thư mục đó (ví dụ: vị trí icons, bg-image, dạng tên file,...)

Vậy thì giờ chỉ cần xóa `.htaccess` và thêm `.DS_Store` vào và ấn Enter:

![[Pasted image 20251109103947.png]]

-> Mảnh cuối cùng: `_35844447}`

=> Flag: `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_35844447}`