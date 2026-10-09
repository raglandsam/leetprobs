-- Write your PostgreSQL query statement below
with stats as (select d.name as Department , e.name as Employee, e.salary as Salary, 
dense_rank() over ( partition by d.id order by e.salary desc) 
    as sal_ranks
from department d join employee e on e.departmentId=d.id) 
select Department, Employee, Salary 
from stats 
where sal_ranks <= 3;