import requests

def obtener_clima(ciudad, api_key):
    # URL de la API de OpenWeatherMap con el endpoint para obtener el clima actual
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    
    # Hacer la solicitud GET a la API
    respuesta = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        datos = respuesta.json()
        
        # Extraer la información relevante
        temperatura = datos['main']['temp']
        descripcion = datos['weather'][0]['description']
        humedad = datos['main']['humidity']
        viento = datos['wind']['speed']
        
        # Mostrar la información del clima
        print(f"Clima en {ciudad}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Descripción: {descripcion}")
        print(f"Humedad: {humedad}%")
        print(f"Velocidad del viento: {viento} m/s")
    else:
        # Mostrar un mensaje de error si la solicitud no fue exitosa
        print("Error al obtener el clima. Verifica el nombre de la ciudad y tu API key.")

if __name__ == "__main__":
    api_key = "0642faa3c2268ef1a828111b4c7115f6"
    ciudad = "Monterrey"
    obtener_clima(ciudad, api_key)