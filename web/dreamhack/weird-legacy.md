# weird legacy
url-parse and URL (whatwg) is legacy, when a string outside the isValid range exists during the hostname parsing process, the hostname parsing is stopped and / is added in front of the remaining string.

```
http://host8.dreamhack.games:9781/fetch?url=http://webhook.site*.localhost
```
