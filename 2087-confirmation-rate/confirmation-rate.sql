-- Write your PostgreSQL query statement below
--select s.user_id as user_id, round(,2) from signups s join confirmations c

with stats as 
(select s.user_id,
count(s.user_id) filter (where c.action='confirmed') as cnf_count,
count(c.user_id) as req_count 
from signups s left join confirmations c on s.user_id=c.user_id group by s.user_id) 
select user_id, (case 
                    when req_count > 0 then round(cnf_count::numeric/req_count,2)
                    else 0
                end) as confirmation_rate from stats;