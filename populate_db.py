import requests
import json

# Propiedades de muestra
propiedades = [
    {
        "titulo": "Casa Moderna en Zona Norte",
        "descripcion": "Hermosa casa de 3 habitaciones con jardín privado y cochera para 2 autos",
        "precio": 250000,
        "ubicacion": "Zona Norte",
        "imagen_url": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400"
    },
    {
        "titulo": "Apartamento Centro Histórico",
        "descripcion": "Apartamento completamente renovado en el corazón de la ciudad",
        "precio": 180000,
        "ubicacion": "Centro",
        "imagen_url": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=400"
    },
    {
        "titulo": "Villa con Piscina",
        "descripcion": "Espectacular villa de lujo con piscina infinita y vistas panorámicas",
        "precio": 450000,
        "ubicacion": "Zona Este",
        "imagen_url": "https://images.unsplash.com/photo-1613977257363-707ba9348227?w=400"
    },
    {
        "titulo": "Casa Familiar Zona Sur",
        "descripcion": "Amplia casa familiar perfecta para criar hijos, con patio grande",
        "precio": 320000,
        "ubicacion": "Zona Sur",
        "imagen_url": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=400"
    },
    {
        "titulo": "Loft Industrial",
        "descripcion": "Moderno loft en edificio industrial renovado, ideal para profesionales",
        "precio": 195000,
        "ubicacion": "Centro",
        "imagen_url": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=400"
    },
    {
        "titulo": "Casa de Campo",
        "descripcion": "Tranquila casa de campo con terreno amplio, perfecta para descansar",
        "precio": 280000,
        "ubicacion": "Campo",
        "imagen_url": "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=400"
    }
]

# Agregar todas las propiedades
for prop in propiedades:
    try:
        response = requests.post("http://localhost:5000/api/agregar_propiedad", json=prop)
        if response.status_code == 200:
            print(f"✓ Agregada: {prop['titulo']}")
        else:
            print(f"✗ Error agregando: {prop['titulo']}")
    except Exception as e:
        print(f"Error: {e}")

print("Propiedades de muestra agregadas exitosamente!")