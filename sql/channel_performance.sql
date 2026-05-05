#  Channel performance

select
round(count(distinct o.order_id)/count(distinct g.session_id)*100) as conversion_rate,
g.channel, count(g.session_id) as total_session, count(order_id) as total_order, round(sum(revenue), 2) as total_revenue

 from datavinci_ecom.products

 as p join datavinci_ecom.orders 
 as o on o.product_id= p.product_id
 right join datavinci_ecom.ga4_sessions as g 
 on g.session_id=o.session_id

  group by g.channel;


  