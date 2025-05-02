import requests
import json

# Cargar datos desde archivo
with open('atp_tennis.json', 'r') as f:
    data = json.load(f)

# Lista con todos los documentos sin filtro
lista_datos = data['docs']

base_datos = "poblacion2"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar cada documento individualmente
for doc in lista_datos:
    requests.post(url, headers = headers, json=doc)
