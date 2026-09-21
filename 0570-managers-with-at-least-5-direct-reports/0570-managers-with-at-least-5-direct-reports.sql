# Write your MySQL query statement below
# Write your MySQL query statement below
-- select e1.name
-- from employee e1
-- join employee e2
-- on e1.id=e2.managerId
-- group by e1.name
-- having count(*)>=5;
SELECT NAME 
FROM EMPLOYEE
WHERE ID in (SELECT managerID
            from employee 
            group by managerid
            having count(managerId)>=5
                            
                            );

