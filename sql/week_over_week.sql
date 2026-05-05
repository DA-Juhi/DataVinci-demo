# Week over week revenue (Window function)

with wow as 

(select round(sum(revenue), 2) as total_revenue,
 date_trunc(parse_date('%d-%m-%Y',order_date), WEEK) as order_week 
 from datavinci_ecom.orders group by 2) 

select order_week, 
total_revenue, 
lag(total_revenue) over (order by order_week) as prev_week_revenue,
round(wow.total_revenue-lag(total_revenue) over (order by order_week), 2)as revenue_diff

from wow order by order_week;