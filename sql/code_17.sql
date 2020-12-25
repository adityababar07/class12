-- Create table and insert data into it

CREATE TABLE if not exists student(
    ID int Primary Key NOT NULL,
    Name varchar(30) NOT NULL,
    Age int NOT NULL,
    Gender char(1) NOT NULL,
    Address varchar(50) NOT NULL, 
    Phone_number char(10) ,
    Email_address varchar(20) ,
    CONSTRAINT chk_stu CHECK (Age<=20 AND Gender in ('m','f','o'))
);

INSERT INTO test.student VALUES (01,'Jhonny',17,'m','sangli','1452367895','jhonny@gmail.com');
INSERT INTO test.student VALUES (02,'arvind',16,'m','miraj','7485425614','arvind@gmail.com');
INSERT INTO test.student VALUES (03,'saloni',18,'f','ashta','8547956514','saloni@gmail.com');
INSERT INTO test.student VALUES (04,'jackson',17,'m','bedag','1578469853','jackson@gmail.com');

SELECT * FROM test.student;

CREATE TABLE if not exists student_marks(
    ID int primary key NOT NULL,
    Marks int NOT NULL
);

INSERT INTO test.student_marks VALUES (01,92);
INSERT INTO test.student_marks VALUES (02,95);
INSERT INTO test.student_marks VALUES (03,87);
INSERT INTO test.student_marks VALUES (04,85);

SELECT * FROM test.student_marks;