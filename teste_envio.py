import requests

# URL da sua API no Railway
url = "https://h2ocontrol-api-production.up.railway.app/sensores"

# Dados que queremos enviar
dados = {
    "temperatura": 26.7,
    "distancia": 150.0
}

# Fazendo o POST
resposta = requests.post(url, json=dados)

# Exibindo a resposta
print(resposta.status_code)
print(resposta.json())
