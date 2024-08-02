-- 1
SELECT MIN(OrderDate) AS EarliestDate FROM orders;

-- 2
SELECT COUNT(OrderID) AS TotalOrders FROM orders;

-- 3
CREATE VIEW orderID_totalItems_view AS
SELECT OrderID, sum(quantity) AS sum_of_quantity
FROM orderdetails
GROUP BY OrderID;

SELECT orders.OrderID, table_a.sum_of_quantity AS TotalItem
FROM orders
JOIN orderID_totalItems_view AS table_a
ON orders.OrderID = table_a.OrderID;


SELECT OrderID, SUM(Quantity) AS TotalItem FROM orderdetails
GROUP BY OrderID;


DROP VIEW orderID_totalItems_view;

-- 4
SELECT AVG(sum_of_quantity)
FROM orderID_totalItems_view;


SELECT SUM(quantity) * 1.0/ COUNT(DISTINCT orderId) 
AS AvgItems FROM orderDetails;

-- 5
SELECT OrderID, COUNT(ProductID) AS DistinctItems
FROM orderdetails
GROUP BY OrderID;

-- 6
SELECT Category, AVG(Price) AS AvgPrice
FROM products
GROUP BY Category
HAVING AvgPrice BETWEEN 20 AND 30;

-- 7
SELECT Country, COUNT(Country) AS CustomerCount
FROM customers
GROUP BY Country
HAVING CustomerCount > 10 and Country != '';

-- 8
SELECT CustomerID, COUNT(OrderID) AS Ordered
FROM orders
GROUP BY CustomerID
ORDER BY Ordered desc;

-- 9
SELECT ProductID, COUNT(OrderID) AS Ordered
FROM orderdetails
GROUP BY ProductID
HAVING Ordered > 10
ORDER BY ProductID asc;

-- 10
SELECT ProductID, SUM(Quantity) AS TotalItems
FROM orderdetails
WHERE ProductID = 1
GROUP BY ProductID;