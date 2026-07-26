# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary
from Employee e
left join Department d
on e.departmentId=d.id
join(
    select departmentId,
    Max(salary) as max_salary
    from employee
    group by departmentId
)m
on e.departmentId=m.departmentId
and e.salary=m.max_salary;

