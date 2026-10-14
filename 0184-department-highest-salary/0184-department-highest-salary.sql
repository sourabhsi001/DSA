# Write your MySQL query statement bel
with new_tab as (
                select
                    d.name as Department,
                    e.name as Employee,
                    e.salary,
                    dense_rank() over (partition by e.departmentId order by e.salary desc) as rnk
                from employee e 
                join Department d
                on e.departmentId=d.id
)

select department,employee,salary
from new_tab
where rnk=1;
