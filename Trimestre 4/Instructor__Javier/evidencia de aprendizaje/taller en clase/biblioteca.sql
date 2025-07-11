create database tarde;
use tarde;

create table usuarios(
	nombre varchar(30),
    clave varchar (30),
    primary key (nombre)
    );

create table clavesanteriores(
	numero int auto_increment,
    nombre varchar(30),
    clave varchar(30),
    primary key (numero)
     );
   
delimiter //   
create trigger before_usuarios_update
	before update
    on usuarios
    for each row
begin before_ventas_insert
insert into clavesanteriores(nombre,clave) values (old.nombre,old.clave);
end
// delimiter ;

insert into usuarios(nombre,clave) values ('marcos','123abc') ;
update usuarios set clave='123456asd' where nombre='marcos';  

insert into ventas (codigolibro, precio, cantidad) values (1,15,1);

  Delimiter //
create trigger  before_ventas_delete
before delete
on ventas  
for each row
begin
  update libros set stock = libros.stock+old.cantidad
  where old.codigolibro=libros.codigo;
  end //
  delimiter ;
 
  delete from ventas where numero =1;


    