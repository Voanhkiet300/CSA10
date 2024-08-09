-- 1
SELECT o.OrderId, c.CustomerID, c.CustomerName, c.Country
FROM orders AS o INNER JOIN customers AS c
ON o.CustomerID = c.CustomerID
GROUP BY o.OrderID;


-- 2
SELECT c.Country, COUNT(Country) AS Ordered
FROM orders AS o INNER JOIN customers AS c
ON o.CustomerID = c.CustomerID
GROUP BY Country
ORDER BY Ordered DESC;


-- 3
SELECT p.ProductID, p.ProductName, o.Quantity, p.Price
FROM orderdetails As o INNER JOIN products AS p
on o.ProductID = p.ProductID
WHERE o.OrderID = 10248;


-- 4
SELECT o.OrderID, SUM(o.Quantity * p.Price) AS TotalAmount
FROM orderdetails AS o INNER JOIN products AS p
ON o.ProductID = p.ProductID
WHERE o.OrderID = 10248;


-- 5
SELECT od.OrderID, SUM(od.Quantity * p.Price) AS TotalAmount
FROM orders AS o INNER JOIN orderdetails AS od INNER JOIN products AS p
ON od.ProductID = p.ProductID AND o.OrderID = od.OrderID
WHERE o.OrderDate = '1996-07-08'
GROUP BY o.OrderID;


-- 6
SELECT o.OrderId, c.CustomerID, o.OrderDate
FROM orders AS o INNER JOIN customers AS c
ON o.CustomerID = c.CustomerID
WHERE c.Country = 'Argentina' AND o.OrderDate < '1996-08-01'
GROUP BY o.OrderID;


-- 7
SELECT p1.ProductID, p1.ProductName, p1.Price
FROM products AS p1 INNER JOIN products AS p2
GROUP BY p1.ProductID
HAVING p1.Price > AVG(p2.Price)
ORDER BY p1.Price ASC;


-- 8
SELECT o.OrderID, o.CustomerID, o.OrderDate
FROM orders AS o INNER JOIN orderdetails AS od INNER JOIN products AS p
ON od.ProductID = p.ProductID AND o.OrderID = od.OrderID
WHERE p.CategoryID = 4
GROUP BY o.OrderID
ORDER BY o.OrderID;


-- 9
SELECT c.CustomerID, c.CustomerName
FROM orders AS o 
	INNER JOIN orderdetails AS od 
	INNER JOIN products AS p 
    INNER JOIN customers AS c
ON od.ProductID = p.ProductID AND o.OrderID = od.OrderID AND o.CustomerID = c.CustomerID
WHERE p.CategoryID = 4
GROUP BY o.OrderID
ORDER BY c.CustomerID;


