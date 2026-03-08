#!/usr/bin/env python3
"""
Script de verificación completa del sitio web de bienes raíces
"""
import requests
import sys
import time

BASE_URL = "http://localhost:5000"

def test_endpoint(name, method, url, data=None, expected_status=200):
    """Prueba un endpoint y retorna si pasa o falla"""
    try:
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json=data)
        else:
            print(f"❌ {name}: Método no soportado")
            return False

        if response.status_code == expected_status:
            print(f"✅ {name}: OK")
            return True
        else:
            print(f"❌ {name}: Status {response.status_code} (esperado {expected_status})")
            return False
    except Exception as e:
        print(f"❌ {name}: Error - {e}")
        return False

def main():
    print("🚀 Verificando sitio web de bienes raíces de Miriam Vazquez")
    print("=" * 60)

    # Esperar a que el servidor esté listo
    print("⏳ Esperando que el servidor inicie...")
    time.sleep(2)

    tests_passed = 0
    total_tests = 0

    # Test 1: Página principal
    total_tests += 1
    if test_endpoint("Página principal", "GET", f"{BASE_URL}/"):
        tests_passed += 1

    # Test 2: Página de admin
    total_tests += 1
    if test_endpoint("Página admin", "GET", f"{BASE_URL}/admin.html"):
        tests_passed += 1

    # Test 3: Login correcto
    total_tests += 1
    login_data = {"usuario": "miriam", "contraseña": "Miriam*1"}
    if test_endpoint("Login admin", "POST", f"{BASE_URL}/api/login", login_data):
        tests_passed += 1

    # Test 4: Login incorrecto
    total_tests += 1
    bad_login_data = {"usuario": "admin", "contraseña": "wrong"}
    response = requests.post(f"{BASE_URL}/api/login", json=bad_login_data)
    if response.status_code == 200 and not response.json().get("success"):
        print("✅ Login incorrecto rechazado: OK")
        tests_passed += 1
    else:
        print("❌ Login incorrecto: No rechazado correctamente")

    # Test 5: Obtener propiedades
    total_tests += 1
    if test_endpoint("Obtener propiedades", "GET", f"{BASE_URL}/api/propiedades"):
        tests_passed += 1

    # Test 6: Agregar propiedad
    total_tests += 1
    prop_data = {
        "titulo": "Test Property",
        "descripcion": "Propiedad de prueba",
        "precio": 100000,
        "ubicacion": "Test",
        "imagen_url": "test.jpg"
    }
    if test_endpoint("Agregar propiedad", "POST", f"{BASE_URL}/api/agregar_propiedad", prop_data):
        tests_passed += 1

    # Test 7: Contacto
    total_tests += 1
    contact_data = {"name": "Test", "email": "test@test.com", "message": "Test message"}
    if test_endpoint("Contacto", "POST", f"{BASE_URL}/api/contact", contact_data):
        tests_passed += 1

    print("=" * 60)
    print(f"📊 Resultados: {tests_passed}/{total_tests} pruebas pasaron")

    if tests_passed == total_tests:
        print("🎉 ¡Todas las pruebas pasaron! El sitio está funcionando correctamente.")
        print("\n📋 Próximos pasos:")
        print("1. El sitio está listo para deployment")
        print("2. Crea una cuenta en Railway.app")
        print("3. Conecta tu repositorio GitHub")
        print("4. Railway desplegará automáticamente")
        print("5. Apunta tu dominio de Hostinger al URL de Railway")
        return True
    else:
        print("⚠️  Algunas pruebas fallaron. Revisa los errores arriba.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)