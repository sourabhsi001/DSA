# Write your MySQL query statement below
with new_tab as(
                select 
                    salary,
                    dense_rank() over (order by salary desc) as rnk
                from employee
)
select max(salary) as SecondHighestSalary 
from new_tab
where rnk=2;