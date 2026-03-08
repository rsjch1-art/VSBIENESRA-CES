const express = require("express");
const app = express();

// Middleware para JSON
app.use(express.json());

// Ruta raíz para healthcheck
app.get("/", (req, res) => {
  res.send("Servicio activo ✅");
});

// Ejemplo de endpoint de propiedades
app.get("/api/propiedades", (req, res) => {
  res.json([
    {
      id: 1,
      titulo: "Casa en Metepec",
      precio: 2500000,
      ubicacion: "Metepec, Edo. Mex.",
      metros: 200,
      cuartos: 3,
      banos: 2,
      estacionamiento: 2,
      imagen_url: "https://via.placeholder.com/400",
      nota: "NO incluye gastos de escritura"
    }
  ]);
});

// Puerto dinámico de Railway
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en puerto ${PORT}`);
});
