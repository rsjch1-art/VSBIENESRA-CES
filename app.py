import os
import psycopg2

# Lee la variable de entorno que Railway inyecta
DATABASE_URL = os.environ.get("DATABASE_URL")

# Conéctate usando esa URL
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
