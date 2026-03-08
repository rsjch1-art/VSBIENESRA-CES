import requests
import json

# Probar login
url = "http://localhost:5000/api/login"
data = {"usuario": "miriam", "contraseña": "Miriam*1"}

try:
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)

# Agregar propiedad de prueba
prop_data = {
    "titulo": "Casa Moderna en Zona Norte",
    "descripcion": "Hermosa casa de 3 habitaciones con jardín",
    "precio": 250000,
    "ubicacion": "Zona Norte",
    "imagen_url": "https://example.com/casa1.jpg"
}

try:
    response = requests.post("http://localhost:5000/api/agregar_propiedad", json=prop_data)
    print("Agregar Status:", response.status_code)
    print("Agregar Response:", response.json())
except Exception as e:
    print("Error agregar:", e)

# Probar obtener propiedades
try:
    response = requests.get("http://localhost:5000/api/propiedades")
    print("Propiedades Status:", response.status_code)
    print("Propiedades:", response.json())
except Exception as e:
    print("Error propiedades:", e)