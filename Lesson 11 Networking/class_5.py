# Implementing Authorization Headers
import requests


data = {
    "username": "mohammed@example.com",
    "password": "qwerty123"
}

token = requests.post("https://traveller.talrop.works/api/v1/auth/token/", data=data)

log_info = token.json()

# access token
access = log_info["access"]

headers = {
    "Authorization": f"Bearer {access}"
}

protected_request = requests.get("https://traveller.talrop.works/api/v1/places/protected/30/", headers=headers)

print(protected_request.json())