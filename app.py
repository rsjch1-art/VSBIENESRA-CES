from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2
import os

app = Flask(__name__)

# --- Configuración de PostgreSQL ---
DB_URL = os.environ.get("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DB_URL)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS propiedades (
            id SERIAL PRIMARY KEY,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            precio NUMERIC,
            ubicacion TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_db()

# --- Rutas principales ---
@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM propiedades")
    propiedades = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", propiedades=propiedades)

@app.route("/propiedad/<int:prop_id>")
def propiedad(prop_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM propiedades WHERE id=%s", (prop_id,))
    propiedad = cursor.fetchone()
    cursor.close()
    conn.close()
    if propiedad:
        return render_template("propiedad.html", propiedad=propiedad)
    else:
        return "Propiedad no encontrada", 404

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        titulo = request.form["titulo"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        ubicacion = request.form["ubicacion"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO propiedades (titulo, descripcion, precio, ubicacion) VALUES (%s, %s, %s, %s)",
            (titulo, descripcion, precio, ubicacion)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("home"))
    return render_template("agregar.html")

@app.route("/eliminar/<int:prop_id>", methods=["POST"])
def eliminar(prop_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM propiedades WHERE id=%s", (prop_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("home"))

# --- Endpoint de salud ---
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

# --- Inicialización ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
