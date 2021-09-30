/*Проанализировать запросы, которые выполнялись на занятии, определить возможные корректировки и/или улучшения (JOIN пока не применять).*/
/*Пусть задан некоторый пользователь. 
Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.*/
select 
	* 
from 
	users 
where id = 
	(select
		id
	from
		(select 
			distinct(count(*)) val,
			id
		from 
			(select 
				if(from_user_id = 101, to_user_id, from_user_id) id
			from
				messages
			where 
				from_user_id = 101 or to_user_id = 101) m
		where id in 
			(select 
				if(initiator_user_id = 101, target_user_id, initiator_user_id) id
			from
				friend_requests
			where
				initiator_user_id = 101 or target_user_id = 101)
		group by id
		order by val
		limit 1) s
	);

/*Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.
*/
select 
	count(*)
from 
	likes
where 
	media_id in 
		(select 
			id 
		from 
			media as m
		inner join
				(select
					user_id
				from
					profiles
				order by
					datediff(current_timestamp(), birthday) 
				limit 10) as u
		on m.user_id = u.user_id
		); 
		
/*Определить кто больше поставил лайков (всего) - мужчины или женщины?*/
select 
	(select 
		count(*)
	from
		likes l
	where
		l.user_id in
		(select 
			user_id
		from 
			profiles
		where 
			profiles.gender = 'f')) 
	f,
	(select 
		count(*)
	from
		likes l
	where
		l.user_id in
		(select 
			user_id 
		from 
			profiles
		where 
			profiles.gender = 'm')) 
	m;
	
/*Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.*/
