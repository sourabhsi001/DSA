# Write your MySQL query statement below
select e1.name,
    b1.bonus
from employee as e1
left join bonus b1
on e1.empid=b1.empid
where bonus<1000 or bonus is null;

-- SELECT e.name,
--        b.bonus
-- FROM Employee e
-- LEFT JOIN Bonus b
-- ON e.empId = b.empId
-- WHERE b.bonus < 1000
--    OR b.bonus IS NULL;
