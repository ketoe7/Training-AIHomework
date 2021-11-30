# Resolve MAC Address

The purpose of this project is to implement two services: PingService and ReceiverService. The first one is able to send HTTP requests to any URL on the internet. ReceiverService is a basic pingable REST application, which returns {"Receiver": "Cisco is the best!"}.

## Getting started

To be able to use the application, user needs to run a following command:
```shell
docker-compose up
```

## Features

* Both services are Python, accompanied by Flask-RESTX framework. (Although the task suggests to use Flask-RESTPlus, this version of the framework is out of date. Hence it was decided to use the new official fork Flask-RESTX, which is being supported nowadays)
* PinService provides two endpoints: 
1. /api/v1/ping - accepts a POST method, accepting a body which contains a url key and corresponding link, I.E. {'url': 'https://www.foobar.com'}
2. /api/v1/health - accepts a GET method, returning "healthy" status when PingService is active
* ReceiverService provides an endpoint: 
1. /api/v1/info - accepts a GET method and returns {"Receiver": "Cisco is the best!"}.
* Tests folder contains one pytest test, which validates wether the following command 
```shell
curl -X POST http://localhost:8080/api/v1/ping -H "Content-Type: application/json" -d '{"url":"http://ReceiverService:8080/api/v1/info"}'
```
returns {“Receiver”: “Cisco is the best!”}. 
* Additionally the services provide a built-in tool, allowing to try out the API requests.

## Useful Links

- Flask RESTX documentation: https://flask-restx.readthedocs.io/en/latest/index.html
