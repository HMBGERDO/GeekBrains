/*��������� ������ ������������� users, ������� ����������� ���� �� ���� ����� orders � �������� ��������.*/
select
	*
from 
	users u
join
	orders o 
on 
	u.id = o.user_id;
		
/*�������� ������ ������� products � �������� catalogs, ������� ������������� ������.*/
select 
	p.name name,
	c.name cat
from 
	products p 
join 
	catalogs c
on 
	p.catalog_id = c.id;