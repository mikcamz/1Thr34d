# Dream Gallery
This challenge involves bypassing LFI filter

## Solve
since `file://` and `flag` is filtered, our payload will become:
```
file:/%66lag.txt
```

set the title as anything and url as the payload. Then copy the image's link and decode it:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/961802466611a84bd5ec780e555b8613ce5142888047bb6fc75e6e751f7ea84f.png)
