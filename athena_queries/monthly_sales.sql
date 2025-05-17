SELECT 
  Product,
  Region,
  SUM(Revenue) AS TotalRevenue,
  COUNT(OrderID) AS Orders
FROM processed_sales_data
GROUP BY Product, Region
ORDER BY TotalRevenue DESC;
