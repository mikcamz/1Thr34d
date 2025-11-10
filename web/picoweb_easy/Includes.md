#### Description

Can you get the flag?Go to this [website](http://saturn.picoctf.net:55207/) and see what you can discover.

Hint:
Is there more code than what the inspector initially shows?

#inspector

---

À với bài này, tác giả muốn nhấn mạnh khái niệm mới dưới đây:
#### **"Include directive"** (Chỉ thị Bao gồm):

Khái niệm "Include"
    Tác giả đang nhấn mạnh rằng trong nhiều ngôn ngữ lập trình, có các lệnh như `include`, `copy`, hoặc `import` để chèn nội dung của một file khác vào file gốc. Điều này chính là cách mà file HTML của trang web bạn đang xem đã liên kết (include) các file CSS và JavaScript vào nội dung của nó.
    -> Khuyến khích tính đóng gói (encapsulation) và tái sử dụng mã (reuse of code)
    
Áp dụng cho Web
    Trong ngữ cảnh phát triển web, điều này có nghĩa là:
    - HTML là xương sống (file gốc).
    - CSS và JavaScript là các "included files" (thường là các `<link>` hoặc `<script>` tags) chứa các quy tắc định dạng và logic lập trình riêng biệt.

Vì thế giờ tôi nhảy sang tab `Sources` để đọc 2 file js và css (vì html không có dấu hiện flag), và tôi tìm thấy flag sau (ghép 2 mảnh ở 2 bên lại):

=> `picoCTF{1nclu51v17y_1of2_f7w_2of2_6edef411}`