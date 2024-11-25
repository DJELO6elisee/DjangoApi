import requests
# from getpass import getpass

# endpoint = "http://127.0.0.1:8001/product/auth/"
# username = input("Entrer votre nom d'utilisateur :\n")
# password = getpass("Entrer un mot de passe :\n")

# auth_response = requests.post(endpoint, json = {'username':username, 'password':password})
# print(auth_response.json())
# print(auth_response.status_code)

# if auth_response.status_code == 200:
endpoint = "http://127.0.0.1:8001/product/listcreate/"
headers = {'Authorization': 'Bearer bec1dd92dee486e60c51f9b368a59ffdafeff8ea'}

response = requests.get(endpoint, headers=headers)
print(response.json())

print(response.status_code)