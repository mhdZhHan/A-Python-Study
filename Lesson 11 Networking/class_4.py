# Requests Post Method
import requests


data = {
    "username": "mohammed@example.com",
    "password": "qwerty123"
}

r = requests.post("https://traveller.talrop.works/api/v1/auth/token/", data=data)


login_info = r.json()
# print(login_info)

access = login_info["access"]
print(access)