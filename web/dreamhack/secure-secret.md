# Secure Secret
This challenge involves decrypting Flask's cookie to get flag path

## Solve
The code set our session cookie as our flag path
```python
def get_index():
    # safely save the secret into session data
    session['secret'] = flag_path
```   

obtain the session cookie:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/54bc9a6f89009d7d331fbb15c9c4a7e4b931c6583e0b548c6db69cd899e166fe.png)

And decode the first part to get the path to the flag
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/04d5171a852fae6f34f927c12fcfbd738cc5519fcc2d911d0e8fa6141e9515e1.png)


