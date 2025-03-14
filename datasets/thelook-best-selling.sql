SELECT oi.product_id as product_id, p.name as product_name, p.category as product_category, count(*) as num_of_orders
FROM `bigquery-public-data.thelook_ecommerce.products` as p 
JOIN `bigquery-public-data.thelook_ecommerce.order_items` as oi
ON p.id = oi.product_id
GROUP BY 1,2,3
ORDER BY num_of_orders DESC