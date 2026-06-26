CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT)
AS $$
declare calc INT;
BEGIN
    if n <=0 then
        return;
    end if;
    calc := Case when N>0 then N-1 else 0 END;
    
    RETURN QUERY (
    
    -- Write your PostgreSQL query statement below.
    select (select distinct e.Salary from employee e order by e.Salary desc limit 1 offset calc)
      
  );
END;
$$ LANGUAGE plpgsql;