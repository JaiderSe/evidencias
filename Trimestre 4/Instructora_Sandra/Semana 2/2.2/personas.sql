-- 1. Crear la base de datos
CREATE DATABASE PersonaBD;

-- 2. Usar la base de datos
USE PersonaBD;

-- 3. Crear la tabla 'persona'
CREATE TABLE persona (
    codigo INT PRIMARY KEY,
    nombre VARCHAR(100),
    fecha_nacimiento DATE
);

-- 4. Describir la estructura de la tabla
-- (Este comando se ejecuta para mostrar la estructura. No necesita terminar en punto y coma en algunas plataformas)
DESCRIBE persona;

-- 5. Mostrar todas las tablas en la base de datos
SHOW TABLES;

-- 6. Insertar 15 registros en la tabla 'persona'
INSERT INTO persona (codigo, nombre, fecha_nacimiento) VALUES
(1, 'Laura González', '1995-06-15'),
(2, 'Carlos Méndez', '1990-04-10'),
(3, 'Ana Torres', '1988-12-23'),
(4, 'Pedro Suárez', '2000-01-05'),
(5, 'María Castro', '1992-07-18'),
(6, 'Julián Pérez', '1997-11-09'),
(7, 'Claudia Ramírez', '1985-05-30'),
(8, 'Diego Ruiz', '1999-09-14'),
(9, 'Tatiana Mora', '1993-03-03'),
(10, 'Esteban Ríos', '1998-08-22'),
(11, 'Luisa Quintero', '1996-10-01'),
(12, 'Andrés Castaño', '1989-02-17'),
(13, 'Camila Salazar', '2001-04-29'),
(14, 'Fernando Gil', '1991-06-12'),
(15, 'Diana Herrera', '1994-12-05');

-- 7. Consultar todas las personas registradas
SELECT * FROM persona;

-- 8. Crear una tabla para registrar consultas (opcional, útil para logs o auditorías)
CREATE TABLE consultas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(255),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);
