import requests

url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Token 80cebba13b869e1a388afda7daab318fea973fb1'}
r = requests.get(url, headers=headers)
print(r)