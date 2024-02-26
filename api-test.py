import requests

post_data = [{
    "0": 2,
    "1": 3,
    "2": 4
}]

url = 'http://127.0.0.1:5000/squareinput/'

response = requests.post(url, json=post_data)
print('input data: ', post_data)
print('response from the server: ',response.text)