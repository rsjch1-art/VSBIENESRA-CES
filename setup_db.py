#!/usr/bin/env python3
import mysql.connector

# Conectar sin especificar BD para crearla
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  # Cambia si tienes password
)

cursor = conn.cursor()

# Crear BD si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS inmobiliaria")
cursor.execute("USE inmobiliaria")

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS propiedades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2),
    ubicacion VARCHAR(255),
    imagen_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Crear admin por defecto
cursor.execute("DELETE FROM admins WHERE usuario='miriam'")
cursor.execute("INSERT INTO admins (usuario, contraseña) VALUES ('miriam', 'Miriam*1')")

conn.commit()
print("✅ Base de datos creada exitosamente!")
print("👤 Admin creado: miriam / Miriam*1")

cursor.close()
conn.close()