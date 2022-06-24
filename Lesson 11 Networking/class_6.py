# Implementing Search Params
import requests


params = {
    "q": "Tok"
}

r = requests.get("https://traveller.talrop.works/api/v1/places/", params=params)

print(r.json())