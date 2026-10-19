-- Basic monthly sales / financial summary
SELECT
  DATE_TRUNC('month', order_date) AS month,
  SUM(total_amount) AS total_revenue,
  COUNT(DISTINCT customer_id) AS customer_count
FROM orders
GROUP BY 1
ORDER BY 1;