select * from actor;
select actor_id as numero  , first_name as primer_nombre , last_name as segundo_nombre , last_update as actualizar  from actor;
select actor_id as numero , first_name as primer_nombre 
from actor;
select * from customer;
select distinct store_id from customer;
select distinct customer_id from payment;
select  * from country 
order by country desc;
select first_name from customer
order by first_name asc;
select store_id , first_name , last_name from customer;
select  store_id as tienda  , first_name as nombre  ,last_name as apellido from customer;
select last_name as apellido  from customer order by apellido desc;
select *  from actor where first_name like"DAN";
select * from city where city like "london";
select  * from country where country_id = 102;
select * from customer where store_id = 1;
select * from inventory where film_id > 50;
select * from payment  where amount < 3;
select * from payment where amount between 0.01 and 2.99;
select description , release_year from film ;
select * from film where title ="IMPACT ALADDIN";



