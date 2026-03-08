#!/usr/bin/env python3
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="inmobiliaria"
)

cursor = db.cursor()

usuario = "miriam"
contraseña = "Miriam*1"

cursor.execute("DELETE FROM admins WHERE usuario=%s", (usuario,))
cursor.execute("INSERT INTO admins (usuario, contraseña) VALUES (%s,%s)", (usuario, contraseña))

db.commit()

print("Admin creado:")
print(usuario, contraseña)

cursor.close()
db.close()