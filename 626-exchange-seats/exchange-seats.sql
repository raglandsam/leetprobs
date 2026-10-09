-- Write your PostgreSQL query statement below
select id,(case when id%2!=0  then coalesce(lead(student) over (order by id asc), student)
            else lag(student) over (order by id asc) 
             
        end) as Student from seat;  