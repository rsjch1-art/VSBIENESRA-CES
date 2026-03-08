import os
import psycopg2
import urllib.parse as up

DATABASE_URL = os.environ.get("DATABASE_URL")

# Asegúrate que empiece con postgres://
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgres://", 1)

up.uses_netloc.append("postgres")
url = up.urlparse(DATABASE_URL)

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)
cur = conn.cursor()
