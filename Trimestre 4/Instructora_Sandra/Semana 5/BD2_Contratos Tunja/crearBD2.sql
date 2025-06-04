create database contratos;
use contratos;

CREATE TABLE Entidades (
    id_entidad SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    nit VARCHAR(50) UNIQUE,
    tipo_entidad VARCHAR(100)
);


CREATE TABLE Proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    nit VARCHAR(50) UNIQUE,
    tipo_proveedor VARCHAR(100)
);


CREATE TABLE Usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(255) UNIQUE,
    rol VARCHAR(50),
    tipo_cuenta VARCHAR(20) CHECK (tipo_cuenta IN ('Entidad', 'Proveedor')),
    id_entidad BIGINT UNSIGNED,
    id_proveedor BIGINT UNSIGNED,
    FOREIGN KEY (id_entidad) REFERENCES Entidades(id_entidad),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);



CREATE TABLE Procesos (
    id_proceso SERIAL PRIMARY KEY,
    codigo_proceso VARCHAR(100) UNIQUE NOT NULL,
    objeto TEXT,
    id_entidad BIGINT UNSIGNED NOT NULL,
    fecha_apertura DATE,
    estado_proceso VARCHAR(100),
    FOREIGN KEY (id_entidad) REFERENCES Entidades(id_entidad)
);


CREATE TABLE Comentarios (
    id_comentario SERIAL PRIMARY KEY,
    id_proceso BIGINT UNSIGNED NOT NULL,
    id_usuario BIGINT UNSIGNED NOT NULL,
    comentario TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_proceso) REFERENCES Procesos(id_proceso),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);


CREATE TABLE Ofertas (
    id_oferta SERIAL PRIMARY KEY,
    id_proceso BIGINT UNSIGNED NOT NULL,
    id_proveedor BIGINT UNSIGNED NOT NULL,
    valor_oferta NUMERIC(20,2),
    fecha_presentacion DATE,
    FOREIGN KEY (id_proceso) REFERENCES Procesos(id_proceso),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);


CREATE TABLE Contratos (
    id_contrato SERIAL PRIMARY KEY,
    numero_contrato VARCHAR(100) UNIQUE NOT NULL,
    id_proceso BIGINT UNSIGNED NOT NULL,
    id_proveedor BIGINT UNSIGNED NOT NULL,
    objeto TEXT,
    fecha_firma DATE,
    valor_contrato NUMERIC(20,2),
    estado_contrato VARCHAR(100),
    FOREIGN KEY (id_proceso) REFERENCES Procesos(id_proceso),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id_proveedor)
);

INSERT INTO Entidades (nombre, nit, tipo_entidad) VALUES ('MUNICIPIO DE TUNJA/', '891800846', 'Municipio');
INSERT INTO Proveedores (nombre, nit, tipo_proveedor) VALUES ('WILLIAM  ALEXANDER  RAMIREZ  CHAPARRO', '7183949', 'No PYME');
INSERT INTO Contratos (numero_contrato, id_proceso, id_proveedor, objeto, fecha_firma, valor_contrato, estado_contrato) VALUES ('1403 DE 2020', (SELECT id_proceso FROM Procesos WHERE codigo_proceso = 'CO1.BDOS.1591198'), (SELECT id_proveedor FROM Proveedores WHERE nit = '2396872'), 'SUMINISTRO DE DOTACIONES DE VESTIDO DE LABOR Y CALZADO PARA LOS FUNCIONARIOS DE LAS INSTITUCIONES EDUCATIVAS OFICIALES DEL MUNICIPIO DE TUNJA (8.1.1.7).', '12/11/2020', 23591750, 'terminado');
INSERT INTO Procesos (codigo_proceso, objeto, id_entidad, fecha_apertura, estado_proceso) VALUES ('CO1.BDOS.1544194', 'SUMINISTRO DE MATERIAL NECESARIO; PARA LA EJECUCION DE LA ACTIVIDAD DENOMINADA COLOMBIANO DE ORO; A REALIZARCE EL DIA 24 DE NOVIEMBRE DE 2020 EN EL MUNICIPIO DE TUNJA; ESTABLECIDO EN EL ARTICULO 6 DE LA LEY 1091 DE 2006; EN MARCO DEL PROYECTO IMPLEMENTACION DE ESTRATEGIAS QUE CONTRIBUYAN A LA PR', (SELECT id_entidad FROM Entidades WHERE nit = '891800846'), '11/17/2020', 'terminado');
