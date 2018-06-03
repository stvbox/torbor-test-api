To Build:
```
docker build -t test-api https://github.com/sysbes/torbor-test-api.git
```

To Run:
```
docker run -d -p 8080:8080 test-api
```

To Test Sample:

```
http://YOU_DOCKER_HOST_IP:8080/api/fgh8974yhfkh4/city1=Novosibirsk&city2=Kradnodar&price=100
```