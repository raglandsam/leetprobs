-- Write your PostgreSQL query statement below


select t.request_at as "Day",
round(sum(case when t.status like 'cancelled%' then 1 else 0 end)::numeric/ count(*),2) as "Cancellation rate"
from trips t
    join users c on t.client_id=c.users_id
    join users d on t.driver_id=d.users_id
where t.request_at>='2013-10-01' and t.request_at<='2013-10-03' and c.banned='No' and d.banned='No'
group by t.request_at;
