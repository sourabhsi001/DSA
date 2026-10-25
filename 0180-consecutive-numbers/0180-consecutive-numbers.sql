# Write your MySQL query statement below
with new_tab as (
                select 
                    id,
                    num,
                    lag(num,1) over (order by id) as prv1,
                    lag(num,2) over (order by id) as prv2
                from logs
)

select distinct num as ConsecutiveNums 
from new_tab 
where num=prv1 and prv1=prv2;