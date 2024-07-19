-- reed date
-- select all 
select * from customers;
 
-- select special columns 
select city  as customers_city from customers;

-- select distinct (unique data)
select distinct city, country from customers; 
 
-- select with codition
select * from customers where customerId = 3;
select * from customers where customerId between 1 and 3;
select * from orders where OrderDate between '1996-07-04' and '1996-07-06';
select * from products where ProductName like '%g%';

-- select with group by
select city from customers
where City like '%e%'
group by city;

-- select with order by
select * from orderdetails
order by quantity desc			-- lon => nho
-- order by quantity asc		-- nho => lon





