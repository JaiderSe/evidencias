USE Biblioteca;
DROP TABLE IF EXISTS empleados;

CREATE TABLE empleados (
	documento CHAR(8),
	nombre VARCHAR(20),
	apellido VARCHAR(20),
	sueldo DECIMAL(6,2),
	cantidadhijos INT,
	area VARCHAR(30),
	PRIMARY KEY (documento)
);

-- Inserciones válidas
INSERT INTO empleados (documento, nombre, apellido, sueldo, cantidadhijos, area)
VALUES 
('22222222','Juan','Perez',300,2,'Contaduria'),
('22333333','Ana','Lopez',700,0,'Contaduria'),
('22444444','Marta','Perez',500,1,'Sistemas'),
('22555555','Susana','Garcia',400,2,'Secretaria'),
('22666666','Jose Maria','Morales',1200,3,'Secretaria');


DELIMITER //
CREATE PROCEDURE cantidad_hijos(
	IN p_documento char(8),
    INOUT cantidad int)
BEGIN
SELECT cantidadhijos + cantidad INTO cantidad
FROM empleados
WHERE documento = p_documento;
END//
DELIMITER ;

set @cant=0;

call cantidad_hijos('22222222', @cant);
select @cant;

call cantidad_hijos('22666666', @cant);
select @cant;

create table clientes(
codigo int unsigned auto_increment,
nombre varchar (30) not null,
domicilio varchar (30),
ciudad varchar (20),
codigoprovincia tinyint unsigned,
telefono varchar (11),
primary key (codigo)
);

insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Lopez Marcos', 'Colon 111', 'Córdoba',1,'null');
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Perez Ana', 'San Martin 222', 'Cruz del Eje',1,'4578585');
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Garcia Juan', 'Rivadavia 333', 'Villa Maria',1,'4578445');
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Perez Luis', 'Sarmiento 444', 'Rosario',2,null);
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Pereyra Lucas', 'San Martin 555', 'Cruz del Eje',1,'4253685');
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Gomez Ines', 'San Martin 666', 'Santa Fe',2,'0345252525');
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Torres Fabiola', 'Alem 777', 'Villa del Rosario',1,'4554455');
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Lopez Carlos', 'Irigoyen 888', 'Cruz del Eje',1,null);
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Ramos Betina', 'San Martin 999', 'Cordoba',1,'4223366');
 insert into clientes (nombre,domicilio,ciudad,codigoProvincia,telefono)
  values ('Lopez Lucas', 'San Martin 1010', 'Posadas',4,'0457858745');

create table provincias(
codigo tinyint unsigned auto_increment,
nombre varchar (20),
primary key (codigo)
);

insert into provincias (nombre) values ('Cordoba');
insert into provincias (nombre) values ('Santa Fe');
insert into provincias (nombre) values ('Corrientes');
insert into provincias (nombre) values ('Misiones');
insert into provincias (nombre) values ('Salta');
insert into provincias (nombre) values ('Buenos Aires');
insert into provincias (nombre) values ('Neuquen');

DELIMITER //
CREATE PROCEDURE cantidad_cliente_provincias(
IN provincias1 varchar(20),
IN provincias2 varchar(20))
BEGIN
DECLARE canti1 int;
DECLARE canti2 int;

SELECT count(*) INTO canti1 FROM clientes as cli
JOIN provincias as pro
ON pro.codigo = cli.codigoprovincia
WHERE pro.nombre = provincias1;
	SELECT count(*) INTO canti1 FROM clientes as cli
	JOIN provincias as pro
	ON pro.codigo = cli.codigoprovincia
	WHERE pro.nombre = provincias2;
		SELECT canti1, canti2;
END //
DELIMITER ;

/***********************26/06/2025***********************/
DELIMITER //
CREATE PROCEDURE mas_cliente_provincias(
IN provincias1 varchar(20),
IN provincias2 varchar(20))
BEGIN
DECLARE canti1 int;
DECLARE canti2 int;

SELECT count(*) INTO canti1 FROM clientes as cli
JOIN provincias as pro
ON pro.codigo = cli.codigoprovincia
WHERE pro.nombre = provincias1;
	SELECT count(*) INTO canti2 FROM clientes as cli
	JOIN provincias as pro
	ON pro.codigo = cli.codigoprovincia
	WHERE pro.nombre = provincias2;
		IF canti1 > canti2 THEN 
			SELECT provincias1, canti1;
		ELSEIF canti2 > canti1 THEN 
			SELECT provincias2, canti2;
		ELSE 
			SELECT provincias1, provincias2, canti1;
		END IF;
END //
DELIMITER ;

Call mas_cliente_provincias('Cordoba', 'Santa Fe');
Call mas_cliente_provincias('Salta', 'Buenos Aires');

DELIMITER //
CREATE PROCEDURE tipo_medalla
BEGIN
CASE opuesto
WHEN 1 THEN
	SET tipo='oro'
WHEN 2 THEN
	SET tipo='plata'
WHEN 3 THEN
	SET tipo='bronce'
END CASE;
END //
DELIMITER;

CALL tipo_medalla(1,@tip);
select @ti;