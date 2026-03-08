from flask import Flask, render_template, request, redirect, url_for, jsonify
import psycopg2, os

app = Flask(__name__)
DB_URL = os.environ.get("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DB_URL)

def init_db():
    try:
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
    except Exception as e:
        print("⚠️ Error inicializando DB:", e)

# --- Rutas ---
@app.route("/")
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM propiedades")
        propiedades = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("index.html", propiedades=propiedades)
    except Exception as e:
        return f"Error conectando a DB: {e}", 500

@app.route("/health")
def health():
    # No depende de la DB, siempre responde
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    init_db()
    app.run(host="0.0.0.0", port=port)
