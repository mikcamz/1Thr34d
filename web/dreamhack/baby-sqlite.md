## baby-sqlite
This challenge involves bypassing sqli filter

Since we can't escape string because `'` is filtered, we will inject into the `level` param which datatype is number.

In the code there are no mention of user admin being inserted into the db, so we have to union our own admin userr

## Solve
Those lead me to this payload
```
uid=x&upw=x&level=0/**/union/**/values(char(97)||char(100)||char(109)||char(105)||char(110))
```

- Uses C type comment `/**/` to replace whitespace
- `||` for concatenating chars
- Since AND have higher precedence in sql, this OR clause will be able to influence the whole query
- SQLite support UNION without SELECT => `union values(...)` to inject a new row

POST this and you will get the flag baby-sqlite
