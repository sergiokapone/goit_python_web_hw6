-- Список курсів, які певному студенту читає певний викладач.
SELECT teachers.teacher_name,subjects.subject_name, students.student_name
FROM subjects
JOIN grades ON grades.subject_id = subjects.subject_id
JOIN students ON students.student_id = grades.student_id
JOIN teachers ON teachers.teacher_id = subjects.teacher_id
WHERE students.student_name = ? AND teachers.teacher_name = ?
GROUP BY subjects.subject_name
