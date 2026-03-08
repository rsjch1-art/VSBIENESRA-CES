from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="../frontend")
app.secret_key = os.getenv("SECRET_KEY", "miriam_real_estate_2026")

def db():
    return sqlite3.connect("inmobiliaria.db")

# Inicializar BD
def init_db():
    conn = db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        contraseña TEXT NOT NULL
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS propiedades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        precio REAL,
        ubicacion TEXT,
        imagen_url TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    # Crear admin por defecto
    cur.execute("INSERT OR IGNORE INTO admins (usuario, contraseña) VALUES (?, ?)", ("miriam", "Miriam*1"))
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return send_from_directory("../frontend","index.html")

@app.route("/admin.html")
def admin():
    return send_from_directory("../frontend","admin.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("../frontend",path)

@app.route("/api/login", methods=["POST"])
def login():
    try:
        data=request.json
        conn=db()
        cur=conn.cursor()
        cur.execute("SELECT * FROM admins WHERE usuario=? AND contraseña=?",(data["usuario"], data["contraseña"]))
        result=cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"success": result is not None, "error": None if result else "Credenciales inválidas"})
    except Exception as e:
        return jsonify({"success":False, "error":str(e)}), 500

@app.route("/api/propiedades")
def propiedades():
    try:
        conn=db()
        conn.row_factory = sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM propiedades")
        data=cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([dict(row) for row in data])
    except Exception as e:
        return jsonify([]), 500

@app.route("/api/agregar_propiedad", methods=["POST"])
def agregar():
    try:
        data=request.json
        conn=db()
        cur=conn.cursor()
        cur.execute("""INSERT INTO propiedades (titulo,descripcion,precio,ubicacion,imagen_url) 
                      VALUES (?,?,?,?,?)""",(data["titulo"],data["descripcion"],data["precio"],data["ubicacion"],data.get("imagen_url","")))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"success":True})
    except Exception as e:
        return jsonify({"success":False, "error":str(e)}), 500

@app.route("/api/eliminar_propiedad", methods=["POST"])
def eliminar():
    try:
        data=request.json
        conn=db()
        cur=conn.cursor()
        cur.execute("DELETE FROM propiedades WHERE id=?",(data["id"],))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"success":True})
    except Exception as e:
        return jsonify({"success":False, "error":str(e)}), 500

@app.route("/api/logout", methods=["POST"])
def logout():
    return jsonify({"success":True})

@app.route("/api/contact", methods=["POST"])
def contact():
    try:
        data=request.json
        return jsonify({"success":True, "message":"Mensaje recibido"})
    except:
        return jsonify({"success":False}), 500

if __name__=="__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_ENV") == "development")