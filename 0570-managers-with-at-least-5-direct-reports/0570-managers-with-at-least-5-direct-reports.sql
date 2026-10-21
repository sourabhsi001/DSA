# Write your MySQL query statement
SELECT NAME 
FROM EMPLOYEE
WHERE ID in (SELECT managerID
            from employee 
            group by managerid
            having count(managerId)>=5
                            
                            );