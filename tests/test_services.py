import requests

ping_service = 'http://localhost:8080/api/v1/ping'
receiver_service = 'http://receiver-service:8080/api/v1/info'


def test_ping_receiver():
    expected_response = {'Receiver': 'Cisco is the best!'}
    data = {'url': receiver_service}
    response = requests.post(ping_service, json=data)
    print(response.json())
    assert expected_response == response.json()
