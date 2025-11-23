# development-env
This challenge involves leaking hardcoded secret and forging jwt key

# Solve
/validate endpoint
```
app.post("/validate", async (req, res) => {
  try {
    let contentType = req.header("Content-Type").split(";")[0];
    if (
      ["multipart/form-data", "application/x-www-form-urlencoded"].indexOf(
        contentType
      ) === -1
    ) {
      throw new Error("content type not supported");
    } else {
      let bodyKeys = Object.keys(req.body);
      if (bodyKeys.indexOf("id") === -1 || bodyKeys.indexOf("pw") === -1) {
        throw new Error("missing required parameter");
      } else {
        if (
          typeof database[req.body["id"]] !== "undefined" &&
          database[req.body["id"]] === req.body["pw"]
        ) {
          if (
            req.get("User-Agent").indexOf("MSIE") > -1 ||
            req.get("User-Agent").indexOf("Trident") > -1
          )
            throw new Error("IE is not supported");
          jwt = await cryptolib.generateJWT(req.body["id"], "FAKE_KEY");
          res
            .cookie("auth", jwt, {
              maxAge: 30000,
            })
            .send(
              "<script>alert('success');document.location.href='/'</script>"
            );
        } else {
          res.json({ message: "error", detail: "invalid id or password" });
        }
      }
    } catch (e) {
    if (isDevelopmentEnv) {
      res.status(500).json({
        message: "devError",
        detail: JSON.parse(parsetrace(e, { sources: true }).json()),
      });
    } else {
      res.json({ message: "error", detail: e });
    }
  }
});
 ...
 ```
 As you can see, the secret key used to sign the jwt key is hardcoded, and the isDevelopmentEnv print out all error trace when error. Note the way the endpoint through error when our User-Agent is MSIE or Trident

Leaking the jwt signing key:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/91ae3a354a3284eb3fd14e79e27d7d5d6212d25525e9a27d485c31087050463c.png)

Use it to forge a new key:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/b0cbf1a4eb36d2d277aae769f88e592e64d8212041283db2a8e9cb28edab72b3.png)

Submit and get the flag
