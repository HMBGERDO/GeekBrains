/*Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.*/
select
	*
from 
	users u
join
	orders o 
on 
	u.id = o.user_id;
		
/*Выведите список товаров products и разделов catalogs, который соответствует товару.*/
select 
	p.name name,
	c.name cat
from 
	products p 
join 
	catalogs c
on 
	p.catalog_id = c.id;