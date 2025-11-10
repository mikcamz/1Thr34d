# easy-login

This challenge involves messing with PHP7 type juggling.

![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/9ad0bfad94eb746776f901214fb7f45ce96d4af1883071437e81f49f8c78d9e5.png)

As you can see, when the code try to compare our OTP and the global string otp, if our input is `true` (boolean), the `!=` will always return true.

To bypass the strcmp() function, if you pass in an array, the strcmp will return NULL, but in PHP7, `!NULL` will become true:)

Modify the redirect request from index php to control the raw data being sent:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/135a8e9f66fe597334586a9e1ee6868b643915ba5c0b076ae126e6cba3ce884e.png)
