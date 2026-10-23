# Write your MySQL query statement below
with new_tab as (
                select student,class,count(student) as cnt
                from courses
                group by class
)
select class
from new_tab
where cnt>=5;