-- Write your PostgreSQL query statement below
with stats as (select d.name as Department, e.name as Employee,e.salary as Salary,dense_rank() over (partition by d.id order by salary desc) as sal_ranks from employee e join department d on e.departmentId=d.id)
select department,employee, salary from stats where sal_ranks =1