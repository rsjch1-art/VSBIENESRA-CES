const express = require("express");
const cors = require("cors");
const mysql = require("mysql2/promise");

const app = express();
app.use(cors());
app.use(express.json());

// Conexión a MySQL (Railway te da variables de entorno)
const pool = mysql.createPool({
  host: process.env.MYSQLHOST || "localhost",
  user: process.env.MYSQLUSER || "root",
  password: process.env.MYSQLPASSWORD || "",
  database: process.env.MYSQLDATABASE || "inmobiliaria",
  port: process.env.MYSQLPORT || 3306
});

// ✅ Ruta raíz para healthcheck
app.get("/", (req, res) => {
  res.send("Servicio activo ✅");
});

// 📋 Obtener propiedades
app.get("/api/propiedades", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT * FROM propiedades");
    res.json(rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Error al obtener propiedades" });
  }
});

// 🛠️ Agregar propiedad
app.post("/api/agregar_propiedad", async (req, res) => {
  try {
    const { titulo, descripcion, precio, ubicacion, metros, cuartos, banos, estacionamiento, tipo, imagen_url } = req.body;
    await pool.query(
      "INSERT INTO propiedades (titulo, descripcion, precio, ubicacion, metros, cuartos, banos, estacionamiento, tipo, imagen_url) VALUES (?,?,?,?,?,?,?,?,?,?)",
      [titulo, descripcion, precio, ubicacion, metros, cuartos, banos, estacionamiento, tipo, imagen_url]
    );
    res.json({ success: true });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Error al guardar propiedad" });
  }
});

// 🚪 Puerto dinámico de Railway
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en puerto ${PORT}`);
});
