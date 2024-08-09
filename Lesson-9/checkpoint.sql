-- Câu 1:
CREATE TABLE Employees (
	EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    HireDate DATE
);

DROP TABLE employees;

-- Câu 2:
ALTER TABLE Employees
ADD COLUMN Salary DECIMAL(10, 2) DEFAULT 0.00;

INSERT INTO employees VALUES (1, 'A', 'Nguyen Van', '2000-8-14', 20),
							(2, 'B', 'Nguyen Van', '2000-8-14', 18);
-- Câu 3:
SELECT * FROM Employees;

-- Câu 4:
SELECT MAX(Salary) FROM employees;

-- Câu 5:
SELECT MIN(Salary) FROM employees;

-- Câu 6:
SELECT COUNT(EmployeeID) FROM employees;

-- Câu 7:
SELECT SUM(Salary) FROM employees;

-- Câu 8:
SELECT e.EmployeeID, e.FirstName, e.LastName, d.DepartmentName
FROM Employees AS e INNER JOIN Departments AS d
ON e.DepartmentID = d.DepartmentID;

-- Câu 9:
SELECT e.EmployeeID, e.FirstName, e.LastName, d.DepartmentName
FROM Employees AS e LEFT JOIN Departments AS d
ON e.DepartmentID = d.DepartmentID;

-- Câu 10:
ALTER TABLE Employees
MODIFY COLUMN Salary FLOAT;