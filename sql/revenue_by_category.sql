# Revenue by category

select ROUND(SUM(revenue), 2) as total_revenue, count(o.product_id)as total_order, category from datavinci_ecom.orders as o 
join datavinci_ecom.products as p 
on o.product_id=p.product_id
group by category
order by sum(revenue) desc; 


