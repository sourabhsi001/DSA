# Write your MySQL query statement below
select Department,Employee,salary
from(
    select 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        DENSE_RANK() over (Partition by departmentId order by e.salary desc ) as rnk
    from employee as e
    join department as d
    on e.departmentId=d.id
) as ranked_table
where rnk<=3;