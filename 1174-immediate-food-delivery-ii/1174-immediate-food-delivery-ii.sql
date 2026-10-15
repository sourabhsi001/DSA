with new_tab as (
                select 
                    customer_id,
                    min(order_date) as first_order_date
                from Delivery
                group by customer_id
    )
select round(sum(case
                    when n.first_order_date=d.customer_pref_delivery_date then 1 else 0 end)*100/count(*),2)as immediate_percentage 
from new_tab n
join Delivery d
on n.customer_id=d.customer_id
AND n.first_order_date=d.order_date ;