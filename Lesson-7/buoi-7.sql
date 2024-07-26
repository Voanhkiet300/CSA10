-- sum: tong so luong mon hang theo ProductID (orderDetails)
CREATE VIEW product_quantity_view AS
SELECT ProductID, sum(quantity) AS sum_of_quantity
FROM orderdetails
GROUP BY ProductID;
-- operators: thong tin product(name, unit, price);
-- price * quantity
SELECT productName AS name, unit, price * table_a.sum_of_quantity as total
from products join (
	SELECT ProductID, SUM(quantity) as "sum_of_quantity"
    from orderdetails
    GROUP BY ProductID) as table_a
on products.ProductID = table_a.ProductID;

SELECT productName AS name, unit, price * table_a.sum_of_quantity as total
from products join product_quantity_view as table_a
on products.ProductID = table_a.ProductID;

-- max: order cuoi cung (gan nhat)
SELECT MAX(OrderDate) AS max_OrderDate from orders;

-- toan bo thong tin 
SELECT * FROM orders
WHERE OrderDate = (
	SELECT MAX(OrderDate) AS max_OrderDate FROM orders
);





-- avg: lay product co price lon hon trung binh
SELECT * FROM products WHERE Price > (
	SELECT AVG(Price) AS avg_price FROM products);
    
    
    
-- gia trung binh tung loai sp > 30
select category, avg(price) as avg_price
from products group by category 
having avg_price > 30;

-- union: lien ket du lieu 2 bang
-- union: lay du lieu ko trung lap (unique)
SELECT MAX(price) AS range_price FROM products
UNION
SELECT MIN(price) from products;


