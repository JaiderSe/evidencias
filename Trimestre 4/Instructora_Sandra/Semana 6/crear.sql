CREATE TABLE Empleados (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE Proyectos (
    id_proyecto INT PRIMARY KEY,
    id_empleado INT,
    nombre_proyecto VARCHAR(100)
);
INSERT INTO Empleados (id_empleado, nombre) VALUES
(1, 'Ana'),
(2, 'Juan'),
(3, 'Laura');

INSERT INTO Proyectos (id_proyecto, id_empleado, nombre_proyecto) VALUES
(1, 2, 'App Móvil'),
(2, 3, 'Sitio Web'),
(3, NULL, 'Infraestructura');
SELECT Empleados.nombre, Proyectos.nombre_proyecto
FROM Empleados
RIGHT JOIN Proyectos
ON Empleados.id_empleado = Proyectos.id_empleado;
