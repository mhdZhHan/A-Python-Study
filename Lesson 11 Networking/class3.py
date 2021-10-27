# Requests Get Method
import requests


r = requests.get("https://traveller.talrop.works/api/v1/places/")

print(r) # <Response [200]>

# print(r.text)
# print(r.json())
print(type(r.json())) # <class 'dict'>