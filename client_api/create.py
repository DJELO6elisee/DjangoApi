import requests

endpoint = "http://127.0.0.1:8001/product/create/"
response = requests.post(endpoint)
print(response.json())

print(response.status_code)