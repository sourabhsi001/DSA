# Write your MySQL query statement below
select e2.name 
from employee as e1
join employee as e2
on e1.managerid=e2.id
group by e2.id,e2.name
having count(*)>=5;