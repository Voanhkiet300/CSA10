-- sever => database => schema => table => prob --

CREATE DATABASE school;
USE school;

ALTER DATABASE school
READ ONLY = 0;
CREATE TABLE students (
	id VARCHAR(12) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    firstname VARCHAR(255) NOT NULL
);

select *
from students;

ALTER TABLE students
add column lastname varchar(100);

ALTER TABLE students
modify lastname varchar(100)
after firstname;

alter table students
rename column id to student_id;


create table classes (
	class_id varchar(12) primary key,
    class_title varchar(50) not null,
    class_description varchar(200)
);

select *
from classes;

-- bang ket hop class >< student
create table enrollments (
	enrollment_id varchar(12) primary key,
	student_id varchar(12) not null,
    class_id varchar(12) not null,
    constraint foreign key (student_id)
    references students(student_id),
    constraint foreign key (class_id)
    references classes(class_id)
);

select *
from enrollments;

-- xoa, sua
drop table classes; 

drop table enrollments;

-- tao lai bang enrollments
create table enrollments (
	enrollment_id varchar(12) primary key,
	student_id varchar(12) not null,
    class_id varchar(12) not null
);

alter table enrollments
add constraint foreign key (student_id)
references students(student_id);

alter table enrollments
add constraint foreign key (class_id)
references classes(class_id);


-- tao du lieu
insert into students(student_id, firstname, lastname)
values ('000111', 'Nguyen', 'Van B');

update students
set email = 'vanb@gmail.com'
where student_id = '000111';

select * from students;





