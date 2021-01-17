-- 19. Joining two tables using select statement and applying arithmetic operations

select student.Name, student_marks.Phy_marks, student_marks.chem_marks, student_marks.maths_marks, student_marks.Phy_marks + student_marks.chem_marks +student_marks.maths_marks as 'Total'
from student, student_marks
where student.ID=student_marks.ID; 

