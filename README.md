# monty_hall_problem
API for check Monty Hall problem

https://en.wikipedia.org/wiki/Monty_Hall_problem


Example:
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"choose_option":"keep","attempts":100000}' http://localhost:5000/play
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 29
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Thu, 22 Apr 2021 22:43:20 GMT

{"loose":66729,"wins":33271}
```
