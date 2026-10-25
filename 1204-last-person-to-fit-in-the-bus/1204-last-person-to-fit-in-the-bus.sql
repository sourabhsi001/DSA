# Write your MySQL query statement below
with new_tab as (
                select *,
                    sum(weight) over  (order by turn) as tw
                from queue
                

)
select person_name
from new_tab
where tw<=1000
order by turn desc
limit 1;
