import requests

endpoint = "http://127.0.0.1:8001/product/update/1/"
response = requests.put(endpoint)
print(response.json())

print(response.status_code)