create database personasBD;
use personasBD;

create table persona(
id int(10),
nombre varchar(30),
fecha_nacimiento date 
);
describe persona;
insert into persona (id, nombre, fecha_nacimiento) values
('1', 'juan', '2000-02-01'),
( 2,'Juan Pérez', '2005-02-24'), 
(3, 'María Gómez', '2005-03-04'),
(4,'Sandra López',  '2015-03-07'),
(5,'Emilio lopez',  '2016-03-07'),
(6,'Manuel Ortiz',  '2017-03-07'),
(7,'Carlos Tacuma',  '2018-03-07'),
(8,'Lina Ortega',  '2019-03-07'),
(9,'Carlos López',  '2014-03-07'),
(10, 'Ana Maria Torres', '1996-03-07'),
(11, 'Emily Torres', '1996-03-07'),
(12, 'mariana Tacuma', '1997-03-07'),
(13, 'Natalia Tabarez', '1995-03-07'),
(14, 'juana Perez', '1994-03-07'),
(15, 'Ana Coronel', '1993-03-07');
select*from persona;

select id AS identificacion, nombre AS NombreCliente FROM persona;
SELECT count(*) AS Total from persona;
SELECT count(*) AS DespuesDel2000 from persona where (fecha_nacimiento>'2000-01-01');
SELECT nombre from persona where (nombre like "%lo%");
SELECT*from persona where (nombre like "M%");
SELECT*from persona where (fecha_nacimiento between "2005-01-01" and "2005-06-30") order by fescha_nacimiento desc;
SELECT*from persona where (select YEAR(fecha_nacimiento)%2=0) order by fescha_nacimiento desc;
SELECT NOW() AS FechaActual;
SELECT*from persona where (select year(fecha_nacimiento-now())>"18");
SELECT*from persona where (fecha_nacimiento between "2007-01-01" and now());
SELECT*from persona where (year(now())-year(fecha_nacimiento))>18;
SELECT length("Pepe") AS Cantidad_Caracteres;
select*from persona where(select length(nombre)>"10");


TRUNCATE TABLE persona;

