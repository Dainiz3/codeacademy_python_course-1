import requests
import json

url = "localhost:5000/"

payload = "payload = {'vardas': 'Donatas', 'pavarde': 'Noreika', 'amzius': 2000}"
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)
