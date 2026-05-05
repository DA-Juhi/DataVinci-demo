# Device performance

with dp as 

(select s.channel as channels, count(s.session_id) as total_sessions,  
round(sum(revenue), 2) as total_revenue, 
round(count(distinct o.order_id)/count(distinct s.session_id) * 100) as conversion_rate 
from datavinci_ecom.ga4_sessions as s
left join datavinci_ecom.orders as o on o.session_id=s.session_id 
group by channels) 

select channels, total_sessions, total_revenue, conversion_rate 
from dp
order by conversion_rate desc;