/*Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, который больше всех общался с выбранным пользователем (написал ему сообщений).*/
select 
	* 
from 
	users u
inner join
		(select 
			distinct(count(*)) val,
			m.id
		from 
			(select 
				if(from_user_id = 101, to_user_id, from_user_id) id
			from
				messages
			where 
				from_user_id = 101 or to_user_id = 101) m
		join  
			(select 
				if(initiator_user_id = 101, target_user_id, initiator_user_id) id
			from
				friend_requests
			where
				initiator_user_id = 101 or target_user_id = 101) f
		on 
			m.id = f.id
		group by m.id
		order by val
		limit 1) s
on
	u.id = s.id;
	
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
	inner join profiles p 
	on l.user_id = p.user_id 
	where p.gender = 'f')
	f,
	(select 
		count(*)
	from
		likes l
	inner join profiles p 
	on l.user_id = p.user_id 
	where p.gender = 'm')
	m;