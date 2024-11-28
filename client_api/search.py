import requests

endpoint = "http://127.0.0.1:8001/search/search_api/?q=banane"
response = requests.post(endpoint)
print(response.json())

print(response.status_code)