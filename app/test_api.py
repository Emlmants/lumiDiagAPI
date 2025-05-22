import requests
import json

url = "http://10.20.20.250:8000/predict/"

# Exemple de données
input_data = {
    "Infrarouge": 68,
    "Rouge": 511,
    "Temperature": 35.1,

}

response = requests.post(
    url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(input_data)
)

if response.status_code == 200:
    print("Réponse de l'API :", response.json())
else:
    print("Erreur :", response.status_code)
