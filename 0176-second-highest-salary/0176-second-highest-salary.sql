# Write your MySQL query statement below
select max(Salary) as secondhighestsalary from Employee where salary<(select max(salary) from employee)