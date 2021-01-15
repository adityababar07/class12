-- Create table and insert data into it

CREATE TABLE if not exists student(
    ID int Primary Key NOT NULL AUTO_INCREMENT ,
    Name varchar(30) NOT NULL,
    Age int NOT NULL,
    Gender char(1) NOT NULL,
    Address varchar(50) NOT NULL, 
    Phone_number char(10) ,
    Email_address varchar(20) ,
    CONSTRAINT chk_stu CHECK (Age<=20 AND Gender in ('m','f','o'))
);

INSERT INTO test.student VALUES ('Jhonny',17,'m','sangli','1452367895','jhonny@gmail.com');
INSERT INTO test.student VALUES ('arvind',16,'m','miraj','7485425614','arvind@gmail.com');
INSERT INTO test.student VALUES ('saloni',18,'f','ashta','8547956514','saloni@gmail.com');
INSERT INTO test.student VALUES ('jackson',17,'m','bedag','1578469853','jackson@gmail.com');

SELECT * FROM test.student;

CREATE TABLE if not exists student_marks(
ID int primary key NOT NULL AUTO_INCREMENT ,
Phy_marks int NOT NULL,
chem_marks int NOT NULL,
maths_marks int NOT NULL
);

INSERT INTO test.student_marks VALUES (92,52,58);
INSERT INTO test.student_marks VALUES (95,57,26);
INSERT INTO test.student_marks VALUES (87,78,89);
INSERT INTO test.student_marks VALUES (85,78.96);

SELECT * FROM test.student_marks;