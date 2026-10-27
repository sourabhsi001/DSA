# Write your MySQL query statement below
with new_tab as (
                select 
                    p.product_name,
                    o.order_date,
                    sum(o.unit) as unit
                from products p
                left join orders o
                on p.product_id=o.product_id
                where order_date between '2020-02-01' and '2020-02-29'
                group by product_name
                having sum(o.unit)>=100
)
select product_name,unit
from new_tab;