CREATE DATABASE inmobiliaria;
USE inmobiliaria;

CREATE TABLE admins (
 id INT AUTO_INCREMENT PRIMARY KEY,
 usuario VARCHAR(50),
 contraseña VARCHAR(50)
);

CREATE TABLE propiedades (
 id INT AUTO_INCREMENT PRIMARY KEY,
 titulo VARCHAR(255),
 descripcion TEXT,
 precio DECIMAL(10,2),
 ubicacion VARCHAR(255),
 metros INT,
 cuartos INT,
 banos INT,
 estacionamiento INT,
 tipo VARCHAR(100),
 imagen_url TEXT,
 nota VARCHAR(255) DEFAULT 'NO incluye gastos de escritura'
);