# Write your MySQL query statement below
with top_three as(select 
                     d.name as Department,
                     e.name as Employee,
                     e.salary,
                     dense_rank() over (partition by e.departmentId
                        order by e.salary desc) as rnk 
                   from employee as e
                   join department d
                   on e.departmentId=d.id
)

select Department,Employee,salary
from top_three
where rnk<=3;
