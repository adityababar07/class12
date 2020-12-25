-- Write a SQL program for joining two tables using select statement

select student.Name, student_marks.marks
from student, student_marks
where student.ID=student_marks.ID; 
