import requests

def obtener_imagen_gato(api_key):
    headers = {'x-api-key': api_key}
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200 and data:
        return data[0]["url"]
    else:
        return "Error en la solicitud"

print(obtener_imagen_gato("live_gg7UlZ1zuUFeL6IofPQoNSERRtsKxDJhIskq3ARhpCCESjFSW9y5FZtP7MJPANvm"))