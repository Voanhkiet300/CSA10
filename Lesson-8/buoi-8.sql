
-- tao bang gia
CREATE TABLE a (
	id INT  AUTO_INCREMENT PRIMARY KEY,
    content VARCHAR(100)
);
CREATE TABLE b (
	id INT  AUTO_INCREMENT PRIMARY KEY,
    a_id INT,
    content VARCHAR(100)
);
CREATE TABLE c (
	id INT  AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(500),
    job VARCHAR(50),
    managed_by INT
);

INSERT INTO a(content) VALUES ("a"), ("b"), ("C");
INSERT INTO b(a_id, content) VALUES (1, "a"), (2, "b"), (3, "C");
INSERT INTO c(fullname, job, managed_by)
VALUES ("Nguyen Van A", "cashier", "3"),
("Nguyen Van B", "CEO", NULL),
("Nguyen Van C", "manager", "2"),
("Nguyen Van D", "guide", "3");

DROP TABLE a;
DROP TABLE b;
DROP TABLE c;



-- inner join --
-- lay thong tin khach hang cua tung don hang
SELECT o.OrderID, o.OrderDate, c.CustomerName, c.Address
FROM orders as o INNER JOIN customers as c
ON o.CustomerID = c.CustomerID;

-- left join --
-- lay thong tin cua nhan vien va nhan vien don hang (neu co)
SELECT *
FROM b LEFT JOIN a on a.id = b.a_id;

-- lay thong tin cua nhan vien + thong tin don hang (neu co)
select * 
from employees as e left join orders as o
on e.EmployeeID = o.EmployeeID;

-- self join --
-- lay thong tin cua quan ly nhan vien
SELECT table_1.fullname, table_2.fullname as managed_by
FROM c AS table_1 INNER JOIN c AS table_2
on table_1.managed_by = table_2.id;

SELECT table_1.fullname, table_2.fullname as managed_by
FROM c AS table_1, c AS table_2
WHERE table_1.managed_by = table_2.id;
