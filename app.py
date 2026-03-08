import os, psycopg2, urllib.parse as up
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# --- Configuración de la DB ---
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgres://", 1)

# Conexión psycopg2 (opcional, para pruebas directas)
up.uses_netloc.append("postgres")
url = up.urlparse(DATABASE_URL)
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# --- Flask + SQLAlchemy ---
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)

# Modelo Casa
class Casa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))

# Crear tablas al iniciar
with app.app_context():
    db.create_all()

# --- Rutas de prueba ---
@app.route("/")
def home():
    return "App funcionando 🚀"

@app.route("/test-db")
def test_db():
    try:
        result = db.session.execute("SELECT 1;")
        return f"DB OK: {list(result)}"
    except Exception as e:
        return f"DB ERROR: {e}"

@app.route("/add-casa")
def add_casa():
    nueva = Casa(titulo="Casa demo")
    db.session.add(nueva)
    db.session.commit()
    return "Casa agregada 🚀"

@app.route("/casas")
def casas():
    casas = Casa.query.all()
    return f"Total casas: {len(casas)}"
