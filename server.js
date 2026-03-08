const express = require("express");
const cors = require("cors");
const mysql = require("mysql2/promise");

const app = express();
app.use(cors());
app.use(express.json());

// Conexión a MySQL con variables de entorno de Railway
const pool = mysql.createPool({
  host: process.env.MYSQLHOST,
  user: process.env.MYSQLUSER,
  password: process.env.MYSQLPASSWORD,
  database: process.env.MYSQLDATABASE,
  port: process.env.MYSQLPORT
});

// ✅ Healthcheck
app.get("/", (req, res) => {
  res.send("Servicio activo ✅");
});

// 📋 Obtener propiedades
app.get("/api/propiedades", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT * FROM propiedades");
    res.json(rows);
  } catch (err) {
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
    res.status(500).json({ error: "Error al guardar propiedad" });
  }
});

// 🚪 Puerto dinámico
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor corriendo en puerto ${PORT}`));
