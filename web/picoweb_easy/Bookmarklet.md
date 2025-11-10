#### Description

Why search for the flag when I can make a bookmarklet to print it for me?Browse [here](http://titan.picoctf.net:63468/), and find the flag!

Hints:
1) A bookmarklet is a bookmark that runs JavaScript instead of loading a webpage.
2) What happens when you click a bookmarklet?
3) Web browsers have other ways to run JavaScript too.

#bookmarklet #extension

---

Đây là web tác giả đưa:

![[Pasted image 20251110084852.png]]

Giờ tìm hiểu bookmarklet là gì đã nha=))

**Bookmarklet** là những đoạn mã **JavaScript** nhỏ được lưu trữ dưới dạng một **bookmark** (dấu trang) trong trình duyệt web. Khi ta nhấp vào bookmarklet, nó sẽ thực thi đoạn mã JavaScript đó trên trang web hiện tại, cho phép mình thực hiện các thao tác tùy chỉnh hoặc thay đổi nội dung trang. 

Cú pháp:

```
javascript:(function(){
    // Đoạn code JavaScript của bạn
    // Ví dụ: alert('Hello World!');
})();
```

- `javascript:`: là giao thức đặc biệt báo cho trình duyệt biết rằng nội dung theo sau là mã JavaScript cần được thực thi, thay vì là một URL thông thường.
- `(function(){...})()`: là một Immediately Invoked Function Expression (IIFE). Việc sử dụng IIFE giúp cô lập mã JavaScript này khỏi mã JavaScript hiện có trên trang web, tránh xung đột biến và đảm bảo code chạy ngay lập tức.

Cách sử dụng đây, mình viết cái này thành một dòng rồi dán vào URL bookmark là được:

```   
javascript:(function() {
    var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓË¨ËÓ§Èí";
    var key = "picoctf";
    var decryptedFlag = "";
    for (var i = 0; i < encryptedFlag.length; i++) {
        decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
    }
    alert(decryptedFlag);
})();  
```

->

```
javascript:(function() { var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓË¨ËÓ§Èí"; var key = "picoctf"; var decryptedFlag = ""; for (var i = 0; i < encryptedFlag.length; i++) { decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256); } alert(decryptedFlag); })();
```


![[Pasted image 20251110085643.png]]


Sau khi ấn mở bookmark thì nó sẽ hiện ra flag:

![[Pasted image 20251110090915.png]]

=> `picoCTF{p@g3_turn3r_e8b2d43b}`