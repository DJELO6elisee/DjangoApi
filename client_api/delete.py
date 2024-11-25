import requests

id = input('Enter the id of the product you wanna delete')
endpoint = f"http://127.0.0.1:8001/product/delete/{id}/"
response = requests.delete(endpoint)

print(response.status_code)