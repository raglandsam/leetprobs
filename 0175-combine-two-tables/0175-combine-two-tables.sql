# Write your MySQL query statement below
select  p.lastName, p.firstName , A.city , A.state from Person P left join Address A on P.personId = A.personId;