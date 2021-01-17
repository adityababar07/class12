-- 20. Joining two tables using select statment and applying GROUP BY clause.

select student.ID, student.Name
from student
GROUP BY gender = 'm' or 'f'
