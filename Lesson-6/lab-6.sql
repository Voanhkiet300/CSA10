
-- 1
SELECT * FROM customers WHERE Country = 'Mexico'
LIMIT 0, 5;
-- LIMIT <dong may> <so dong can hien thi>
-- LIMIT <so dong can hien thi>

-- 2
SELECT DISTINCT Country FROM Customers;

-- 3
SELECT * FROM Customers WHERE Country IN ('Canada', 'USA', 'Mexico');

-- 4
SELECT * FROM Customers WHERE Country = 'USA' AND City != 'San Francisco';

-- 5
SELECT ProductName as Name, unit FROM Products;

-- 6
SELECT * FROM Products ORDER BY price ASC;

-- 7
SELECT * FROM Products WHERE category = 'Beverages' ORDER BY price DESC;

-- 8
SELECT * FROM Products WHERE unit like '%boxes%';

-- 9
SELECT * FROM orders WHERE OrderDate like '1996-08-%';

-- 10
SELECT * FROM OrderDetails WHERE ProductID > 10 AND Quantity > 10;
