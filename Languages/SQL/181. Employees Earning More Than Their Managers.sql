/* Write your T-SQL query statement below */
SELECT name as Employee FROM Employee AS E1
WHERE E1.Salary > (SELECT Salary FROM Employee As E2 WHERE E1.managerId = E2.id)