import json
import requests

nauja_uzduotis = {"pavadinimas": "Išplauti indus", "atlikta": False}

r = requests.post("http://127.0.0.1:8000/uzduotis", json=nauja_uzduotis)
print(json.loads(r.text))
